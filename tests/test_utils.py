import shutil
from importlib.util import find_spec, module_from_spec, spec_from_file_location
from pathlib import Path

import matplotlib as mpl
import numpy as np
import pytest
from matplotlib.colors import ListedColormap as LC
from matplotlib.figure import Figure
from matplotlib.legend import Legend

import cmasher as cmr
from cmasher import cm as cmrcm
from cmasher.utils import (
    combine_cmaps,
    create_cmap_mod,
    create_cmap_overview,
    get_bibtex,
    get_cmap_list,
    get_sub_cmap,
    import_cmaps,
    set_cmap_legend_entry,
    take_cmap_colors,
    view_cmap,
)

HAS_VISCM = find_spec("viscm") is not None


def _MPL38_colormap_eq(cmap, other) -> bool:
    # equality check for two colormaps
    # this is adapted from Colormap.__eq__ (mpl 3.8)
    # in previous versions, colormaps compared as != unless they
    # had the exact same name, which is not what we care about here
    from matplotlib.colors import Colormap

    if (
        not isinstance(other, Colormap) or cmap.colorbar_extend != other.colorbar_extend
    ):  # pragma: no cover
        return False
    # To compare lookup tables the Colormaps have to be initialized
    if not cmap._isinit:
        cmap._init()
    if not other._isinit:  # type: ignore [attr-defined] # pragma: no cover
        other._init()  # type: ignore [attr-defined]
    return np.array_equal(cmap._lut, other._lut)  # type: ignore [attr-defined]


# Save the path to this directory
TEST_DIR = Path(__file__).parent

# %% GLOBALS
# Obtain path to directory with colormaps
CMASHER_DIR = Path(cmr.__file__).parent
COLORMAPS_DIR = CMASHER_DIR / "colormaps"

# Obtain list of all colormaps defined in CMasher
# As all colormaps have their own directories, save them instead
_IGNORED = ["PROJECTS", "__pycache__"]
cm_names = [
    p.name
    for p in sorted(COLORMAPS_DIR.glob("*"))
    if p.is_dir() and p.name not in _IGNORED
]

# Obtain list of all colormaps registered in MPL
mpl_cmaps = mpl.colormaps()
mpl_cmaps_as_str: list[str] = list(mpl_cmaps)


# %% PYTEST CLASSES AND FUNCTIONS
# Pytest class for combine_cmaps
class Test_combine_cmaps:
    # Test if multiple Colormaps or colormap names can be combined
    @pytest.mark.parametrize(
        "cmaps, nodes",
        [
            (["Blues", "Oranges", "Greens"], [0.25, 0.75]),
            (["Blues", "Oranges", "Greens"], np.array([0.25, 0.75])),
            (
                [
                    mpl.colormaps["Blues"],
                    mpl.colormaps["Oranges"],
                    mpl.colormaps["Greens"],
                ],
                [0.25, 0.75],
            ),
        ],
    )
    def test_combine_cmaps(self, cmaps, nodes):
        combined_cmap = combine_cmaps(*cmaps, nodes=nodes, n_rgb_levels=256)
        blues_cmap = mpl.colormaps["Blues"]
        oranges_cmap = mpl.colormaps["Oranges"]
        greens_cmap = mpl.colormaps["Greens"]

        assert np.allclose(combined_cmap(0.0), blues_cmap(0))
        assert np.allclose(combined_cmap(0.25), oranges_cmap(0))
        assert np.allclose(combined_cmap(0.75), greens_cmap(0))
        assert np.allclose(combined_cmap(1.0), greens_cmap(255))

        assert combined_cmap.N == 256

    # Test combine cmaps with default nodes
    def test_default_nodes(self):
        combined_cmap = combine_cmaps("Blues", "Oranges", n_rgb_levels=256)

        blues_cmap = mpl.colormaps["Blues"]
        oranges_cmap = mpl.colormaps["Oranges"]

        assert np.allclose(combined_cmap(0.0), blues_cmap(0))
        assert np.allclose(combined_cmap(0.5), oranges_cmap(0))
        assert np.allclose(combined_cmap(1.0), oranges_cmap(255))

    # Test if combining less than 2 colormaps triggers an error
    @pytest.mark.parametrize(
        "cmaps",
        [
            pytest.param([], id="no_cmap"),
            pytest.param(["Blues"], id="single_cmap"),
            pytest.param(["fake_name"], id="fake_cmap_name"),
        ],
    )
    def test_not_enough_cmaps(self, cmaps):
        with pytest.raises(
            ValueError, match="Expected at least two colormaps to combine."
        ):
            combine_cmaps(*cmaps)

    # Test if invalid colormap name raise an error
    def test_invalid_cmap_name(self):
        with pytest.raises(
            KeyError,
            match="'fake_cmap' is not a known colormap name",
        ):
            combine_cmaps("fake_cmap", "Blues")

    # Test if invalid colormap types raise an error
    @pytest.mark.parametrize(
        "invalid_cmap",
        [0, 0.0, [], ()],
    )
    def test_invalid_cmap_types(self, invalid_cmap):
        with pytest.raises(
            TypeError,
            match=f"Unsupported colormap type: {type(invalid_cmap)}.",
        ):
            combine_cmaps("Blues", invalid_cmap)

    # Test if invalid nodes types raise an error
    def test_invalid_nodes_types(self):
        invalid_nodes = "0.5"
        with pytest.raises(
            TypeError,
            match=f"Unsupported nodes type: {type(invalid_nodes)}, expect list of float.",
        ):
            combine_cmaps("Blues", "Greens", nodes=invalid_nodes)

    # Test if mismatch cmaps and nodes length raise an error
    @pytest.mark.parametrize(
        "cmaps, nodes",
        [
            (["Blues", "Oranges", "Greens"], [0.5]),
            (["Reds", "Blues"], [0.2, 0.8]),
        ],
    )
    def test_cmaps_nodes_length_mismatch(self, cmaps, nodes):
        with pytest.raises(
            ValueError,
            match=("Number of nodes should be one less than the number of colormaps."),
        ):
            combine_cmaps(*cmaps, nodes=nodes)

    # Test if invalid nodes raise an error
    @pytest.mark.parametrize(
        "cmaps, nodes",
        [
            (["Blues", "Oranges", "Greens"], [-1, 0.75]),
            (["Blues", "Oranges", "Greens"], [0.25, 2]),
            (["Blues", "Oranges", "Greens"], [0.75, 0.25]),
        ],
    )
    def test_invalid_nodes(self, cmaps, nodes):
        with pytest.raises(
            ValueError,
            match="Nodes should only contain increasing values between 0.0 and 1.0.",
        ):
            combine_cmaps(*cmaps, nodes=nodes)


# Pytest class for create_cmap_mod
class Test_create_cmap_mod:
    # Test if a standalone module can be created
    @pytest.mark.parametrize("name", ["rainforest", "infinity"])
    def test_standalone_copy(self, name, tmp_path):
        # Obtain the currently registered version of rainforest
        cmap_old = mpl.colormaps[f"cmr.{name}"]

        # Create standalone module for rainforest
        cmap_path = create_cmap_mod(
            name,
            save_dir=tmp_path,
            _copy_name=f"{name}_test_copy",
        )

        # Try to import this module
        spec = spec_from_file_location(f"{name}_test_copy", cmap_path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)

        # Check if the colormap in MPL has been updated
        cmap_new = mpl.colormaps[f"cmr.{name}_test_copy"]

        # identity equality isn't achievable since mpl.colormaps.__getitem__
        # may return a copy
        assert cmap_new == mod.cmap

        if mpl.__version_info__ >= (3, 8):
            assert cmap_old == cmap_new
        else:
            assert _MPL38_colormap_eq(cmap_old, cmap_new)

        # Check if the values in both colormaps are the same
        assert np.allclose(cmap_old.colors, cmap_new.colors)

        if name == "infinity":
            # Check that the shifted version of infinity also exists
            assert "cmr.infinity_s" in mpl.colormaps()

    # Test if providing an invalid colormap name fails
    def test_invalid_cmap(self, tmp_path):
        # Check if a ValueError is raised
        with pytest.raises(ValueError):
            create_cmap_mod(
                "this is an incorrect colormap name",
                save_dir=tmp_path,
            )


# Pytest class for create_cmap_overview
class Test_create_cmap_overview:
    # Test if default arguments work
    def test_default(self):
        create_cmap_overview()

    # Test if providing a custom list of colormaps works
    def test_list_no_types(self):
        create_cmap_overview([cmrcm.rainforest], use_types=0, sort="lightness")
        create_cmap_overview(
            ["cmr.rainforest", "cmr.rainforest_r"], use_types=0, title=0
        )

    # Test if providing a custom list of colormaps works
    def test_list_cat(self):
        create_cmap_overview(["cmr.rainforest"])

    # Test if providing all MPL colormap objects works
    @pytest.mark.parametrize("sort", ["perceptual", "lightness"])
    def test_mpl_cmaps_objs(self, sort):
        cmaps = map(mpl.colormaps.__getitem__, mpl_cmaps)
        create_cmap_overview(cmaps, sort=sort)

    # Test if providing all MPL colormap names works
    @pytest.mark.parametrize("cmaps", [mpl_cmaps, mpl_cmaps_as_str])
    @pytest.mark.parametrize("sort", ["perceptual", "lightness"])
    def test_mpl_cmaps_names(self, cmaps, sort):
        create_cmap_overview(cmaps, sort=sort)

    # Test if the lightness profiles can be plotted
    def test_lightness_profiles(self):
        create_cmap_overview(mpl_cmaps, plot_profile=True)

    # Test if dark mode can be enabled for the overview
    def test_dark_mode(self):
        create_cmap_overview([cmrcm.rainforest], dark_mode=True)

    # Test if the grayscale versions can be removed
    def test_no_grayscale(self):
        create_cmap_overview([cmrcm.rainforest], show_grayscale=False)

    # Test if the lightness/perceptual info can be shown
    def test_show_info(self):
        create_cmap_overview([cmrcm.rainforest], show_info=True)

    # Test if providing a custom dict of colormaps works
    def test_dict(self):
        create_cmap_overview({"test1": [cmrcm.rainforest], "test2": ["cmr.rainforest"]})

    # Test if the figure can be saved
    def test_savefig(self, tmp_path):
        dst = tmp_path / "test.png"
        create_cmap_overview(savefig=dst)
        assert dst.is_file()

    # test if providing an invalid sort value raises an error
    def test_invalid_sort_value(self):
        with pytest.raises(ValueError):
            create_cmap_overview(sort="test")


# Pytest for get_bibtex()-function
def test_get_bibtex():
    # Print the output of the get_bibtex() function
    get_bibtex()


# Pytest class for get_cmap_list()-function
class Test_get_cmap_list:
    # Test default arguments
    def test_default(self):
        assert get_cmap_list() == list(cmrcm.cmap_d)

    # Test obtaining all sequential colormaps
    def test_seq(self):
        assert get_cmap_list("seq") == list(cmrcm.cmap_cd["sequential"])

    # Test obtaining all diverging colormaps
    def test_div(self):
        assert get_cmap_list("div") == list(cmrcm.cmap_cd["diverging"])

    # Test obtaining all cyclic colormaps
    def test_cyc(self):
        assert get_cmap_list("cyc") == list(cmrcm.cmap_cd["cyclic"])


# Pytest class for get_sub_cmap()-function
class Test_get_sub_cmap:
    # Test if a copy can be made of the 'rainforest' colormap
    def test_rainforest_copy(self):
        assert np.allclose(
            get_sub_cmap("cmr.rainforest", 0, 1).colors, cmrcm.rainforest.colors
        )

    # Test if a sub can be made
    def test_rainforest_sub(self):
        sub_cmap = get_sub_cmap("cmr.rainforest", 0.2, 0.8)
        assert np.allclose(sub_cmap(0.0), cmrcm.rainforest(51))
        assert np.allclose(sub_cmap(1.0), cmrcm.rainforest(204))
        assert sub_cmap.N == 154

    # Test if a qualitative colormap can be made
    def test_lilac_qual(self):
        qual_cmap = get_sub_cmap("cmr.lilac", 0.2, 0.8, N=5)
        assert np.allclose(qual_cmap(0.0), cmrcm.lilac(51))
        assert np.allclose(qual_cmap(1.0), cmrcm.lilac(204))
        assert qual_cmap.N == 5

    # Test if providing an incorrect range raises an error
    def test_invalid_range(self):
        with pytest.raises(ValueError):
            get_sub_cmap("cmr.rainforest", -1, 1.5)


# Pytest class for import_cmaps()-function
class Test_import_cmaps:
    # Test if all colormaps in cmasher/colormaps are loaded into CMasher/MPL
    @pytest.mark.parametrize("cm_name", cm_names)
    def test_CMasher_cmaps(self, cm_name):
        # Check if provided cm_name is registered in CMasher and MPL
        for name in (cm_name, cm_name + "_r"):
            cmr_cmap = getattr(cmr, name)
            mpl_cmap = mpl.colormaps["cmr." + name]
            assert isinstance(cmr_cmap, LC)
            assert isinstance(mpl_cmap, LC)
            assert getattr(cmrcm, name) is cmr_cmap
            assert cmrcm.cmap_d.get(name) is cmr_cmap
            assert np.allclose(cmr_cmap.colors, mpl_cmap.colors)

    # Test if providing a cmap .npy-file works
    def test_cmap_file_npy(self):
        import_cmaps(
            COLORMAPS_DIR / "cm_rainforest.npy",
            _skip_registration=True,
        )

    def test_resilience(self, tmp_path):
        # check that, in the presence of a npy and a txt,
        # import_cmaps ignores the second
        src = COLORMAPS_DIR / "cm_rainforest.npy"
        shutil.copy(src, tmp_path / "cm_rainforest.npy")
        shutil.copy(src, tmp_path / "cm_rainforest.txt")

        import_cmaps(
            tmp_path,
            _skip_registration=True,
        )

    # Test if providing a cmap .txt-file with 8-bit values works
    def test_cmap_file_8bit(self):
        import_cmaps(TEST_DIR / "data" / "cm_8bit.txt")

    # Test if providing a cmap .txt-file with HEX values works
    def test_cmap_file_HEX(self):
        import_cmaps(TEST_DIR / "data" / "cm_hex.txt")

    # Test if providing a cmap .jscm-file works
    @pytest.mark.skipif(not HAS_VISCM, reason="viscm is required")
    def test_cmap_file_jscm(self):
        cmap_path = TEST_DIR / "data" / "cm_rainforest_jscm.jscm"
        import_cmaps(cmap_path)

    # Test if providing a cyclic colormap works
    def test_cyclic_cmap(self):
        name = "cyclic"
        import_cmaps(TEST_DIR / "data" / f"cm_{name}.txt")
        for cmap in [name, name + "_r", name + "_s", name + "_s_r"]:
            assert "cmr." + cmap in mpl.colormaps()
            assert getattr(cmrcm, cmap, None) is not None
            assert cmap in cmrcm.cmap_d
            assert cmap in cmrcm.cmap_cd["cyclic"]

    # Test if providing a non-existing directory raises an error
    def test_non_existing_dir(self):
        with pytest.raises(OSError):
            import_cmaps("./test")

    # Test if providing an invalid cmap file raises an error
    def test_invalid_cmap_file(self):
        with pytest.raises(OSError):
            import_cmaps(TEST_DIR / "data" / "test.txt")

    # Test if providing an invalid cmap .npy-file raises an error
    def test_invalid_cmap_npy_file(self):
        with pytest.raises(ValueError):
            import_cmaps(TEST_DIR / "data" / "cm_test2.npy")

    # Test if providing a custom directory with invalid cmaps raises an error
    def test_invalid_cmap_dir(self):
        with pytest.raises(ValueError):
            import_cmaps(TEST_DIR / "data")


# Pytest class for set_cmap_legend_entry()-function
class Test_set_cmap_legend_entry:
    # Test if providing a PathCollection object works
    def test_path_collection(self):
        # Create a small scatter plot
        fig = Figure()
        ax = fig.add_subplot()
        plot = ax.scatter([1, 2, 3], [2, 3, 4], c=[3, 4, 5], cmap=cmr.rainforest)

        # Add a cmap legend entry
        set_cmap_legend_entry(plot, "Test")

        # Check if the plot now has a special handler
        assert plot in Legend.get_default_handler_map()

        # Create a legend
        ax.legend()

    # Test if providing a Line2D object does not work
    def test_line2d(self):
        # Create a small line plot
        fig = Figure()
        ax = fig.add_subplot()
        plot = ax.plot([1, 2, 3], [2, 3, 4])

        # Attempt to add the cmap legend entry
        with pytest.raises(ValueError):
            set_cmap_legend_entry(plot, "Test")


# Pytest class for take_cmap_colors()-function
class Test_take_cmap_colors:
    # Test if all colors can be taken from the 'rainforest' colormap
    def test_rainforest_all(self):
        assert np.allclose(
            take_cmap_colors("cmr.rainforest", None), cmr.rainforest.colors
        )

    # Test if five colors can be taken from the 'rainforest' colormap
    def test_rainforest_five(self):
        assert np.allclose(
            take_cmap_colors("cmr.rainforest", 5),
            [
                (0.0, 0.0, 0.0),
                (0.226123592, 0.124584033, 0.562997277),
                (0.0548210513, 0.515835251, 0.45667819),
                (0.709615979, 0.722863985, 0.0834727592),
                (1.0, 1.0, 1.0),
            ],
        )

    # Test if their 8-bit RGB values can be requested as well
    def test_rainforest_five_8bit(self):
        assert np.allclose(
            take_cmap_colors("cmr.rainforest", 5, return_fmt="int"),
            [(0, 0, 0), (58, 32, 144), (14, 132, 116), (181, 184, 21), (255, 255, 255)],
        )

    # Test if their HEX-code values can be requested as well
    def test_rainforest_five_hex(self):
        assert take_cmap_colors("cmr.rainforest", 5, return_fmt="hex") == [
            "#000000",
            "#3A2090",
            "#0E8474",
            "#B5B815",
            "#FFFFFF",
        ]

    # Test if only a subrange can be used for picking colors
    def test_rainforest_sub_five(self):
        assert take_cmap_colors(
            "cmr.rainforest", 5, cmap_range=(0.2, 0.8), return_fmt="hex"
        ) == ["#3E0374", "#10528A", "#0E8474", "#5CAD3C", "#D6BF4A"]

    # Test if providing an incorrect range raises an error
    def test_invalid_range(self):
        with pytest.raises(ValueError):
            take_cmap_colors("cmr.rainforest", 5, cmap_range=(-1, 1.5))


# Pytest class for view_cmap()-function
class Test_view_cmap:
    # Test if default arguments work
    def test_default(self):
        view_cmap("cmr.rainforest")

    # Test if the figure can be saved
    def test_savefig(self, tmp_path):
        dst = tmp_path / "test.png"
        view_cmap(
            "cmr.rainforest",
            show_test=True,
            show_grayscale=True,
            savefig=dst,
        )
        assert dst.is_file()
