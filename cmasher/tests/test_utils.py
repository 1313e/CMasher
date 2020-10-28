# -*- coding: utf-8 -*-

# %% IMPORTS
# Built-in imports
from importlib.util import module_from_spec, spec_from_file_location
import os
from os import path

# Package imports
import cmocean as cmo
import matplotlib.pyplot as plt
from matplotlib import cm as mplcm
from matplotlib.colors import ListedColormap as LC
from matplotlib.legend import Legend
import numpy as np
import pytest

# CMasher imports
import cmasher as cmr
from cmasher import cm as cmrcm
from cmasher.utils import (
    create_cmap_mod, create_cmap_overview, get_bibtex, get_sub_cmap,
    import_cmaps, set_cmap_legend_entry, take_cmap_colors)

# Save the path to this directory
dirpath = path.dirname(__file__)


# %% GLOBALS
# Obtain path to directory with colormaps
cmap_dir = path.abspath(path.join(dirpath, '../colormaps'))

# Obtain list of all colormaps defined in CMasher
# As all colormaps have their own directories, save them instead
cm_names = sorted(next(os.walk(cmap_dir))[1])

# Make sure that the 'PROJECTS' folder is removed
if 'PROJECTS' in cm_names:
    cm_names.remove('PROJECTS')

# Obtain list of all colormaps registered in MPL
mpl_cmaps = plt.colormaps()


# %% PYTEST CLASSES AND FUNCTIONS
# Pytest class for create_cmap_mod
class Test_create_cmap_mod(object):
    # Test if a standalone module of rainforest can be created
    def test_standalone_rainforest(self):
        # Obtain the currently registered version of rainforest
        cmap_old = mplcm.get_cmap('cmr.rainforest')

        # Create standalone module for rainforest
        cmap_path = create_cmap_mod('rainforest')

        # Try to import this module
        spec = spec_from_file_location('rainforest', cmap_path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)

        # Check if the colormap in MPL has been updated
        cmap_new = mplcm.get_cmap('cmr.rainforest')
        assert cmap_new is mod.cmap
        assert cmap_old is not cmap_new

        # Check if the values in both colormaps are the same
        assert np.allclose(cmap_old.colors, cmap_new.colors)

    # Test if providing an invalid colormap name fails
    def test_invalid_cmap(self):
        # Check if a ValueError is raised
        with pytest.raises(ValueError):
            create_cmap_mod('this is an incorrect colormap name')


# Pytest class for create_cmap_overview
class Test_create_cmap_overview(object):
    # Test if default arguments work
    def test_default(self):
        create_cmap_overview()

    # Test if providing a custom list of colormaps works
    def test_list_no_types(self):
        create_cmap_overview([cmrcm.rainforest], use_types=0, sort='lightness')
        create_cmap_overview(['cmr.rainforest', 'cmr.rainforest_r'],
                             use_types=0, title=0)

    # Test if providing a custom list of colormaps works
    def test_list_cat(self):
        create_cmap_overview(['cmr.rainforest'])

    # Test if providing all MPL colormap objects works
    def test_mpl_cmaps_objs(self):
        cmaps = map(mplcm.get_cmap, mpl_cmaps)
        create_cmap_overview(cmaps, sort='alphabetical')

    # Test if providing all MPL colormap names works
    def test_mpl_cmaps_names(self):
        create_cmap_overview(mpl_cmaps, sort='lightness')

    # Test if the lightness profiles can be plotted
    def test_lightness_profiles(self):
        create_cmap_overview(mpl_cmaps, plot_profile=True)

    # Test if providing a custom dict of colormaps works
    def test_dict(self):
        create_cmap_overview({'test1': [cmrcm.rainforest],
                              'test2': ['cmr.rainforest']})

    # Test if the figure can be saved
    def test_savefig(self):
        create_cmap_overview(savefig="test.png")
        assert path.exists("./test.png")


# Pytest for get_bibtex()-function
def test_get_bibtex():
    # Print the output of the get_bibtex() function
    get_bibtex()


# Pytest class for get_sub_cmap()-function
class Test_get_sub_cmap(object):
    # Test if a copy can be made of the 'rainforest' colormap
    def test_rainforest_copy(self):
        assert np.allclose(get_sub_cmap('cmr.rainforest', 0, 1).colors,
                           cmrcm.rainforest.colors)

    # Test if a sub can be made
    def test_rainforest_sub(self):
        sub_cmap = get_sub_cmap('cmr.rainforest', 0.2, 0.8)
        assert np.allclose(sub_cmap(0.0), cmrcm.rainforest(51))
        assert np.allclose(sub_cmap(1.0), cmrcm.rainforest(204))
        assert (sub_cmap.N == 154)

    # Test if providing an incorrect range raises an error
    def test_invalid_range(self):
        with pytest.raises(ValueError):
            get_sub_cmap('cmr.rainforest', -1, 1.5)


# Pytest class for import_cmaps()-function
class Test_import_cmaps(object):
    # Test if all colormaps in cmasher/colormaps are loaded into CMasher/MPL
    @pytest.mark.parametrize('cm_name', cm_names)
    def test_CMasher_cmaps(self, cm_name):
        # Check if provided cm_name is registered in CMasher and MPL
        for name in (cm_name, cm_name+'_r'):
            cmr_cmap = getattr(cmr, name)
            mpl_cmap = mplcm.get_cmap('cmr.'+name)
            assert isinstance(cmr_cmap, LC)
            assert isinstance(mpl_cmap, LC)
            assert getattr(cmrcm, name) is cmr_cmap
            assert cmrcm.cmap_d.get(name) is cmr_cmap
            assert np.allclose(cmr_cmap.colors, mpl_cmap.colors)

    # Test if providing a cmap .txt-file works
    def test_cmap_file_txt(self):
        import_cmaps(path.join(dirpath, '../colormaps/cm_rainforest.txt'))

    # Test if providing a cmap .txt-file with 8-bit values works
    def test_cmap_file_8bit(self):
        import_cmaps(path.join(dirpath, 'data/cm_8bit.txt'))

    # Test if providing a cmap .txt-file with HEX values works
    def test_cmap_file_HEX(self):
        import_cmaps(path.join(dirpath, 'data/cm_hex.txt'))

    # Test if providing a cmap .jscm-file works
    def test_cmap_file_jscm(self):
        cmap_path = path.join(dirpath, 'data/cm_rainforest_jscm.jscm')
        import_cmaps(cmap_path)

    # Test if providing a cyclic colormap works
    def test_cyclic_cmap(self):
        name = 'cyclic'
        import_cmaps(path.join(dirpath, 'data/cm_{0}.txt'.format(name)))
        for cmap in [name, name+'_r', name+'_shifted', name+'_shifted_r']:
            assert 'cmr.'+cmap in plt.colormaps()
            assert getattr(cmrcm, cmap, None) is not None
            assert cmap in cmrcm.cmap_d
            assert cmap in cmrcm.cmap_cd['cyclic']

    # Test if providing a non-existing directory raises an error
    def test_non_existing_dir(self):
        with pytest.raises(OSError):
            import_cmaps('./test')

    # Test if providing an invalid cmap file raises an error
    def test_invalid_cmap_file(self):
        with pytest.raises(OSError):
            import_cmaps(path.join(dirpath, 'data/test.txt'))

    # Test if providing an invalid cmap .npy-file raises an error
    def test_invalid_cmap_npy_file(self):
        with pytest.raises(ValueError):
            import_cmaps(path.join(dirpath, 'data/cm_test2.npy'))

    # Test if providing a custom directory with invalid cmaps raises an error
    def test_invalid_cmap_dir(self):
        with pytest.raises(ValueError):
            import_cmaps(path.join(dirpath, 'data'))


# Pytest class for set_cmap_legend_entry()-function
class Test_set_cmap_legend_entry(object):
    # Test if providing a PathCollection object works
    def test_path_collection(self):
        # Create a small scatter plot
        plot = plt.scatter([1, 2, 3], [2, 3, 4], c=[3, 4, 5],
                           cmap=cmr.rainforest)

        # Add a cmap legend entry
        set_cmap_legend_entry(plot, 'Test')

        # Check if the plot now has a special handler
        assert plot in Legend.get_default_handler_map()

        # Create a legend
        plt.legend()

        # Close the plot
        plt.close()

    # Test if providing a Line2D object does not work
    def test_line2d(self):
        # Create a small line plot
        plot = plt.plot([1, 2, 3], [2, 3, 4])

        # Attempt to add the cmap legend entry
        with pytest.raises(ValueError):
            set_cmap_legend_entry(plot, 'Test')

        # Close the plot
        plt.close()


# Pytest class for take_cmap_colors()-function
class Test_take_cmap_colors(object):
    # Test if all colors can be taken from the 'rainforest' colormap
    def test_rainforest_all(self):
        assert np.allclose(take_cmap_colors('cmr.rainforest', None),
                           cmr.rainforest.colors)

    # Test if five colors can be taken from the 'rainforest' colormap
    def test_rainforest_five(self):
        assert np.allclose(take_cmap_colors('cmr.rainforest', 5),
                           [(0.0, 0.0, 0.0),
                            (0.226123592, 0.124584033, 0.562997277),
                            (0.0548210513, 0.515835251, 0.45667819),
                            (0.709615979, 0.722863985, 0.0834727592),
                            (1.0, 1.0, 1.0)])

    # Test if their 8-bit RGB values can be requested as well
    def test_rainforest_five_8bit(self):
        assert np.allclose(take_cmap_colors('cmr.rainforest', 5,
                                            return_fmt='int'),
                           [(0, 0, 0),
                            (58, 32, 144),
                            (14, 132, 116),
                            (181, 184, 21),
                            (255, 255, 255)])

    # Test if their HEX-code values can be requested as well
    def test_rainforest_five_hex(self):
        assert (take_cmap_colors('cmr.rainforest', 5, return_fmt='hex') ==
                ['#000000', '#3A2090', '#0E8474', '#B5B815', '#FFFFFF'])

    # Test if only a subrange can be used for picking colors
    def test_rainforest_sub_five(self):
        assert (take_cmap_colors('cmr.rainforest', 5, cmap_range=(0.2, 0.8),
                                 return_fmt='hex') ==
                ['#3E0374', '#10528A', '#0E8474', '#5CAD3C', '#D6BF4A'])

    # Test if providing an incorrect range raises an error
    def test_invalid_range(self):
        with pytest.raises(ValueError):
            take_cmap_colors('cmr.rainforest', 5, cmap_range=(-1, 1.5))
