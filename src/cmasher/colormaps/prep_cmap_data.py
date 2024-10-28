import shutil
import sys
from itertools import zip_longest
from pathlib import Path
from textwrap import dedent

import matplotlib.pyplot as plt
import numpy as np
import viscm
from matplotlib.colors import TwoSlopeNorm, to_hex

from cmasher.app_usage import update_tableau_pref_file
from cmasher.cm import cmap_cd
from cmasher.utils import (
    create_cmap_mod,
    create_cmap_overview,
    get_cmap_type,
    register_cmap,
    view_cmap,
)

# %% GLOBALS
docs_dir = Path(__file__).parents[2].joinpath("docs", "source", "user").resolve()


# %% FUNCTION DEFINITIONS
def create_cmap_app_overview():
    # Load sequential image data
    image_seq = np.loadtxt(Path(__file__).parent / "app_data.txt.gz", dtype=int)

    # Obtain resolution ratio
    image_ratio = image_seq.shape[0] / image_seq.shape[1]

    # Create diverging image data
    X, Y = np.meshgrid(
        np.linspace(-2.5, 2.5, image_seq.shape[1]),
        np.linspace(-2, 2, image_seq.shape[0]),
    )
    image_div = (1 - X / 2 + X**5 + Y**3) * np.exp(-(X**2) - Y**2)

    # Obtain all colormaps with their types
    seq_cmaps = list(cmap_cd["sequential"].values())
    div_cmaps = [
        cmap for cmap in cmap_cd["diverging"].values() if not cmap.name.endswith("_r")
    ]
    div_cmaps.extend(
        [cmap for cmap in cmap_cd["cyclic"].values() if not cmap.name.endswith("_r")]
    )

    # Sort colormaps on name
    seq_cmaps.sort(key=lambda x: x.name)
    div_cmaps.sort(key=lambda x: x.name)

    # Determine number of colormaps
    n_seq = len(seq_cmaps)
    n_div = len(div_cmaps)

    # Determine number of columns and rows required
    n_cols = 4
    fontsize = 34
    n_rows_seq = int(np.ceil(n_seq / n_cols))
    n_rows_div = int(np.ceil(n_div / n_cols))
    n_rows = n_rows_seq + n_rows_div

    # Set spacing between the two gridspecs
    gs_spc = 0.5

    # Determine required height of figure
    height = 8.0 * (n_rows / n_cols) * image_ratio + gs_spc

    # Initialize figure
    fig = plt.figure(figsize=(6.4, height))

    # Add gridspecs for the sequential and diverging colormaps
    gs1 = fig.add_gridspec(
        nrows=n_rows_seq,
        ncols=n_cols,
        left=0.10,
        right=0.99,
        top=1 - 0.1 / height,
        wspace=0.05,
        hspace=0,
        bottom=1 - n_rows_seq / n_rows * (1 - gs_spc / height),
    )
    gs2 = fig.add_gridspec(
        nrows=n_rows_div,
        ncols=n_cols,
        left=0.10,
        right=0.99,
        bottom=0.01 / height,
        hspace=0,
        top=(1 - n_rows_seq / n_rows) * (1 - gs_spc / height),
        wspace=0.05,
    )

    # Obtain the Axes objects for the sequential and diverging colormaps
    seq_axs = [fig.add_subplot(x) for x in gs1]
    div_axs = [fig.add_subplot(x) for x in gs2]

    # Make subplot for all sequential colormaps
    for cmap, ax in zip_longest(seq_cmaps, seq_axs):
        # If there is still a colormap left to be plotted, plot it
        if cmap is not None:
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.imshow(image_seq, cmap=cmap)
            ax.set_title(cmap.name)

        # Else, turn the entire Axes object off
        else:
            ax.set_axis_off()

    # Write text specifying that these are sequential colormaps
    x = seq_axs[0].get_position().x0 / 2
    y = (1 + gs1.bottom) / 2
    fig.text(
        x,
        y,
        "Sequential",
        va="center",
        ha="center",
        rotation="vertical",
        color="grey",
        fontsize=fontsize,
        alpha=0.5,
    )

    # Make subplot for all diverging colormaps
    for cmap, ax in zip_longest(div_cmaps, div_axs):
        # If there is still a colormap left to be plotted, plot it
        if cmap is not None:
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.imshow(image_div, cmap=cmap, norm=TwoSlopeNorm(0))
            ax.set_title(cmap.name)

        # Else, turn the entire Axes object off
        else:
            ax.set_axis_off()

    # Write text specifying that these are diverging colormaps
    x = div_axs[0].get_position().x0 / 2
    y = (gs2.top + gs2.bottom + 1 - gs1.top) / 2
    fig.text(
        x,
        y,
        "Diverging/Cyclic",
        va="center",
        ha="center",
        rotation="vertical",
        color="grey",
        fontsize=fontsize,
        alpha=0.5,
    )

    # Obtain figure path
    fig_path_100 = docs_dir / "images" / "cmr_cmaps_app_100.png"
    fig_path_250 = docs_dir.parent / "_static" / "cmr_cmaps_app_250.png"

    # Save the figure
    plt.savefig(fig_path_100, dpi=100)
    plt.savefig(fig_path_250, dpi=250)

    # Close the figure
    plt.close()


# %% MAIN SCRIPT
if __name__ == "__main__":
    # Obtain path to .jscm-file
    jscm_path = Path(sys.argv[1]).resolve()

    # If this path does not exist, try again with added 'PROJECTS'
    if not jscm_path.exists():
        jscm_path = Path("PROJECTS", sys.argv[1])

    # Get colormap name
    name = jscm_path.stem

    # Make a directory for the colormap files
    Path(name).mkdir()

    # Move the .jscm-file to it
    shutil.move(jscm_path, name)

    # Load colormap from .jscm-file
    cmap = viscm.gui.Colormap(None, None, None)
    cmap.load(f"{name}/{name}.jscm")

    # Obtain RGB values of colormap
    v = viscm.viscm_editor(
        uniform_space=cmap.uniform_space,
        cmtype=cmap.cmtype,
        method=cmap.method,
        **cmap.params,
    )
    rgb, _ = v.cmap_model.get_sRGB()

    # Register this colormap in CMasher
    register_cmap(name, rgb)

    # Obtain cmtype
    cmtype = get_cmap_type(f"cmr.{name}")

    # Check if provided cmap is a cyclic colormap
    # If so, obtain its shifted (reversed) versions as well
    if cmtype == "cyclic":
        # Determine the central value index of the colormap
        idx = len(rgb) // 2

        # Shift the entire colormap by this index
        rgb_s = np.concatenate([rgb[idx:], rgb[:idx]], axis=0)

        # Register this colormap as well
        register_cmap(name + "_s", rgb_s)

        # Set cmtype to 'diverging' for the remainder of this script
        cmtype = "diverging"

    # Export as .py-file
    create_cmap_mod(name, save_dir=name)

    # Create colormap figure
    view_cmap("cmr." + name, savefig=f"{name}/{name}.png")

    # Create npy-file with colormap data
    np.save(f"cm_{name}.npy", rgb, allow_pickle=False)

    # Create txt-file with normalized colormap data
    np.savetxt(f"{name}/{name}_norm.txt", rgb, fmt="%.8f")

    # Create txt-file with 8-bit colormap data
    rgb_8bit = np.rint(rgb * 255)
    np.savetxt(f"{name}/{name}_8bit.txt", rgb_8bit, fmt="%i")

    # Create txt-file with HEX colormap data
    rgb_hex = np.apply_along_axis((lambda x: to_hex(x).upper()), 1, rgb)
    np.savetxt(f"{name}/{name}_hex.txt", rgb_hex, fmt="%s")

    # Make new colormap overview
    create_cmap_overview(savefig="cmap_overview.png", sort="lightness")
    create_cmap_overview(
        savefig=docs_dir / "images" / "cmap_overview.png", sort="lightness"
    )
    create_cmap_overview(
        savefig=docs_dir / "images" / "cmap_overview_perceptual.png",
        sort="perceptual",
        show_info=True,
    )
    create_cmap_overview(
        plt.colormaps(),
        plot_profile=True,
        sort="lightness",
        savefig=docs_dir / "images" / "mpl_cmaps.png",
    )
    create_cmap_app_overview()

    # Make string with the docs entry
    docs_entry = dedent(
        """
        .. _{0}:

        {0}
        {1}
        .. image:: ../../../../src/cmasher/colormaps/{0}/{0}.png
            :alt: Visual representation of the *{0}* colormap.
            :width: 100%
            :align: center

        .. image:: ../../../../src/cmasher/colormaps/{0}/{0}_viscm.png
            :alt: Statistics of the *{0}* colormap.
            :width: 100%
            :align: center

        The *{0}* colormap is <visual representation>.
        <Lightness range><colors>
        <Recommended use>"""
    ).format(name, "-" * len(name))

    # Obtain all colormaps with the type of this colormap
    if cmtype == "sequential":
        cmaps = list(cmap_cd["sequential"].values())
    else:
        cmaps = [*cmap_cd["diverging"].values(), *cmap_cd["cyclic"].values()]

    # Make new colormap type overviews
    create_cmap_overview(
        cmaps,
        sort="perceptual",
        use_types=(cmtype == "diverging"),
        savefig=docs_dir / "images" / f"{cmtype[:3]}_cmaps.png",
        title=f"{cmtype.capitalize()} Colormaps",
        show_info=True,
    )
    if cmtype == "sequential":
        cmaps = [cm for cm in plt.colormaps() if get_cmap_type(cm) == "sequential"]
        create_cmap_overview(
            cmaps,
            use_types=False,
            title="Sequential MPL Colormaps",
            savefig=docs_dir / "images" / "seq_mpl_cmaps.png",
        )

    # Update Tableau preferences file
    update_tableau_pref_file(docs_dir.parent / "_static")

    # Create docs entry for this colormap if possible
    try:
        # Create docs entry
        with docs_dir.joinpath(cmtype, f"{name}.rst").open("x") as f:
            f.write(docs_entry[1:])
    # If this file already exists, then skip
    except FileExistsError:
        pass
    # If the file did not exist yet, add it to the corresponding overview
    else:
        # Read the corresponding docs overview page
        docs_overview = docs_dir.joinpath(f"{cmtype}.rst").read_text()

        # Set the string used to start the toctree with
        toctree_header = ".. toctree::\n    :caption: Individual colormaps\n\n"

        # Split the page at where the toctree is located
        desc, _, toctree = docs_overview.partition(toctree_header)

        # Split toctree up into individual lines
        toctree_lines = toctree.splitlines()

        # Add the new entry to toctree
        toctree_lines.append(f"    {cmtype}/{name}")

        # Sort toctree
        toctree_lines.sort()

        # Combine toctree into a single string again
        toctree = "\n".join(toctree_lines)

        # Combine everything together again
        docs_overview = "".join([desc, toctree_header, toctree])

        # Save this as the new docs_overview
        docs_dir.joinpath(f"{cmtype}.rst").write_text(docs_overview)

    # Create viscm output figure
    viscm.gui.main(
        ["view", f"{name}/{name}.jscm", "--save", f"{name}/{name}_viscm.png", "--quit"]
    )
