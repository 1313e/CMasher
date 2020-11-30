# -*- coding: utf-8 -*-

# %% Imports
# Built-in imports
from itertools import zip_longest
import os
from os import path
import shutil
import sys
from textwrap import dedent

# Package imports
from matplotlib.colors import TwoSlopeNorm, to_hex
import matplotlib.pyplot as plt
import numpy as np
import viscm

# CMasher imports
from cmasher.cm import cmap_cd
from cmasher.utils import (
    create_cmap_mod, create_cmap_overview, get_cmap_type, register_cmap)


# %% GLOBALS
docs_dir = path.abspath(path.join(path.dirname(__file__),
                                  '../../docs/source/user'))


# %% FUNCTION DEFINITIONS
def create_cmap_app_overview():
    # Load sequential image data
    image_seq = np.loadtxt(path.join(path.dirname(__file__),
                                     "app_data.txt.gz"), dtype=int)

    # Obtain resolution ratio
    image_ratio = image_seq.shape[0]/image_seq.shape[1]

    # Create diverging image data
    X, Y = np.meshgrid(np.linspace(-2.5, 2.5, image_seq.shape[1]),
                       np.linspace(-2, 2, image_seq.shape[0]))
    image_div = (1-X/2+X**5+Y**3)*np.exp(-X**2-Y**2)

    # Obtain all colormaps with their types
    seq_cmaps = [cmap for cmap in cmap_cd['sequential'].values()]
    div_cmaps = [cmap for cmap in cmap_cd['diverging'].values()
                 if not cmap.name.endswith('_r')]

    # Sort colormaps on name
    seq_cmaps.sort(key=lambda x: x.name)
    div_cmaps.sort(key=lambda x: x.name)

    # Determine number of colormaps
    n_seq = len(seq_cmaps)
    n_div = len(div_cmaps)

    # Determine number of columns and rows required
    n_cols = 4
    fontsize = 34
    n_rows_seq = int(np.ceil(n_seq/n_cols))
    n_rows_div = int(np.ceil(n_div/n_cols))
    n_rows = n_rows_seq+n_rows_div

    # Set spacing between the two gridspecs
    gs_spc = 0.5

    # Determine required height of figure
    height = 8.0*(n_rows/n_cols)*image_ratio+gs_spc

    # Initialize figure
    fig = plt.figure(figsize=(6.4, height))

    # Add gridspecs for the sequential and diverging colormaps
    gs1 = fig.add_gridspec(nrows=n_rows_seq, ncols=n_cols, left=0.10,
                           right=0.99, top=1-0.1/height, wspace=0.05, hspace=0,
                           bottom=1-n_rows_seq/n_rows*(1-gs_spc/height))
    gs2 = fig.add_gridspec(nrows=n_rows_div, ncols=n_cols, left=0.10,
                           right=0.99, bottom=0.01/height, hspace=0,
                           top=(1-n_rows_seq/n_rows)*(1-gs_spc/height),
                           wspace=0.05)

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
    x = seq_axs[0].get_position().x0/2
    y = (1+gs1.bottom)/2
    fig.text(x, y, "Sequential", va='center', ha='center', rotation='vertical',
             color='grey', fontsize=fontsize, alpha=0.5)

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
    x = div_axs[0].get_position().x0/2
    y = (gs2.top+gs2.bottom+1-gs1.top)/2
    fig.text(x, y, "Diverging", va='center', ha='center', rotation='vertical',
             color='grey', fontsize=fontsize, alpha=0.5)

    # Obtain figure path
    fig_path_100 = path.join(docs_dir, 'images', 'cmr_cmaps_app_100.png')
    fig_path_250 = path.join(docs_dir, '../_static', 'cmr_cmaps_app_250.png')

    # Save the figure
    plt.savefig(fig_path_100, dpi=100)
    plt.savefig(fig_path_250, dpi=250)

    # Close the figure
    plt.close()


# %% MAIN SCRIPT
if(__name__ == '__main__'):
    # Obtain path to .jscm-file
    jscm_path = path.abspath(sys.argv[1])

    # If this path does not exist, try again with added 'PROJECTS'
    if not path.exists(jscm_path):
        jscm_path = path.abspath(path.join('PROJECTS', sys.argv[1]))

    # Get colormap name
    name = path.splitext(path.basename(jscm_path))[0]

    # Make a directory for the colormap files
    os.mkdir(name)

    # Move the .jscm-file to it
    shutil.move(jscm_path, name)

    # Load colormap from .jscm-file
    cmap = viscm.gui.Colormap(None, None, None)
    cmap.load("{0}/{0}.jscm".format(name))

    # Obtain RGB values of colormap
    v = viscm.viscm_editor(uniform_space=cmap.uniform_space,
                           cmtype=cmap.cmtype, method=cmap.method,
                           **cmap.params)
    rgb, _ = v.cmap_model.get_sRGB()

    # Register this colormap in CMasher
    register_cmap(name, rgb)

    # Obtain cmtype
    cmtype = get_cmap_type('cmr.{0}'.format(name))

    # Export as .py-file
    create_cmap_mod(name, save_dir=name)

    # Create colormap figure
    fig, ax = plt.subplots(figsize=(12.8, 3.2))
    ax.imshow(rgb[np.newaxis, ...], aspect='auto')
    ax.set_axis_off()
    plt.savefig("{0}/{0}.png".format(name), dpi=100, bbox_inches='tight',
                pad_inches=0)
    plt.close(fig)

    # Create txt-file with colormap data
    np.savetxt("cm_{0}.txt".format(name), rgb, fmt='%.8f')

    # Create txt-file with normalized colormap data
    np.savetxt("{0}/{0}_norm.txt".format(name), rgb, fmt='%.8f')

    # Create txt-file with 8-bit colormap data
    rgb_8bit = np.rint(rgb*255)
    np.savetxt("{0}/{0}_8bit.txt".format(name), rgb_8bit, fmt='%i')

    # Create txt-file with HEX colormap data
    rgb_hex = np.apply_along_axis((lambda x: to_hex(x).upper()), 1, rgb)
    np.savetxt("{0}/{0}_hex.txt".format(name), rgb_hex, fmt="%s")

    # Make new colormap overview
    create_cmap_overview(savefig='cmap_overview.png', sort='lightness')
    create_cmap_overview(
        savefig=path.join(docs_dir, 'images', 'cmap_overview.png'),
        sort='lightness')
    create_cmap_overview(
        plt.colormaps(), plot_profile=True, sort='lightness',
        savefig=path.join(docs_dir, 'images', 'mpl_cmaps.png'))
    create_cmap_app_overview()

    # Make string with the docs entry
    docs_entry = dedent("""
        .. _{0}:

        {0}
        {1}
        .. image:: ../../../../cmasher/colormaps/{0}/{0}.png
            :alt: Visual representation of the *{0}* colormap.
            :width: 100%
            :align: center

        .. image:: ../../../../cmasher/colormaps/{0}/{0}_viscm.png
            :alt: Statistics of the *{0}* colormap.
            :width: 100%
            :align: center

        The *{0}* colormap is <visual representation>.
        <Lightness range><colors>
        <Recommended use>""").format(name, '-'*len(name))

    # Make new colormap type overviews
    create_cmap_overview(
        cmap_cd[cmtype].values(), sort='lightness', use_types=False,
        savefig=path.join(docs_dir, 'images',
                          '{0}_cmaps.png'.format(cmtype[:3])),
        title="{0} Colormaps".format(cmtype.capitalize()))
    if(cmtype == 'sequential'):
        cmaps = [cm for cm in plt.colormaps()
                 if get_cmap_type(cm) == 'sequential']
        create_cmap_overview(
            cmaps, use_types=False, title="Sequential MPL Colormaps",
            savefig=path.join(docs_dir, 'images', 'seq_mpl_cmaps.png'))

    # Create docs entry for this colormap if possible
    try:
        # Create docs entry
        with open(path.join(docs_dir, cmtype,
                            "{0}.rst".format(name)), 'x') as f:
            f.write(docs_entry[1:])
    # If this file already exists, then skip
    except FileExistsError:
        pass
    # If the file did not exist yet, add it to the corresponding overview
    else:
        # Read the corresponding docs overview page
        with open(path.join(docs_dir, "{0}.rst".format(cmtype)), 'r') as f:
            docs_overview = f.read()

        # Set the string used to start the toctree with
        toctree_header = ".. toctree::\n    :caption: Individual colormaps\n\n"

        # Split the page at where the toctree is located
        desc, _, toctree = docs_overview.partition(toctree_header)

        # Split toctree up into individual lines
        toctree = toctree.splitlines()

        # Add the new entry to toctree
        toctree.append("    {0}/{1}".format(cmtype, name))

        # Sort toctree
        toctree.sort()

        # Combine toctree into a single string again
        toctree = '\n'.join(toctree)

        # Combine everything together again
        docs_overview = ''.join([desc, toctree_header, toctree])

        # Save this as the new docs_overview
        with open(path.join(docs_dir, "{0}.rst".format(cmtype)), 'w') as f:
            f.write(docs_overview)

    # Create viscm output figure
    viscm.gui.main(["view", "{0}/{0}.jscm".format(name), "--save",
                    "{0}/{0}_viscm.png".format(name), "--quit"])
