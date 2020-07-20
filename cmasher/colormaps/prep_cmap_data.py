# -*- coding: utf-8 -*-

# %% Imports
# Built-in imports
import os
from os import path
import shutil
import sys
from textwrap import dedent

# Package imports
from matplotlib.cm import cmap_d
import matplotlib.pyplot as plt
import numpy as np
import viscm

# CMasher imports
from cmasher.cm import cmap_cd
from cmasher.utils import create_cmap_overview, get_cmap_type, import_cmaps


# %% GLOBALS
docs_dir = path.abspath(path.join(path.dirname(__file__),
                                  '../../docs/source/user'))


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
    cmtype = cmap.cmtype

    # Convert RGB values to string
    array_str = np.array2string(rgb, max_line_width=79, prefix='cm_data = ',
                                separator=', ', threshold=rgb.size,
                                precision=8)

    # Remove all whitespaces before commas
    for i in range(8, 0, -1):
        array_str = array_str.replace(' '*i+', ', '0'*i+', ')
        array_str = array_str.replace(' '*i+']', '0'*i+']')

    # Export as .py-file
    cm_py_file = dedent("""
        # %% IMPORTS
        # Package imports
        from matplotlib.cm import register_cmap
        from matplotlib.colors import ListedColormap

        # All declaration
        __all__ = ['cmap']

        # Author declaration
        __author__ = "Ellert van der Velden (@1313e)"

        # Package declaration
        __package__ = 'cmasher'


        # %% GLOBALS AND DEFINITIONS
        # Type of this colormap (according to viscm)
        cm_type = "{0}"

        # RGB-values of this colormap
        cm_data = {1}

        # Create ListedColormap object for this colormap
        cmap = ListedColormap(cm_data, name="cmr.{2}", N=len(cm_data))
        cmap_r = cmap.reversed()

        # Register (reversed) cmap in MPL
        register_cmap(cmap=cmap)
        register_cmap(cmap=cmap_r)
        """).format(cmtype, array_str, name)
    with open("{0}/{0}.py".format(name), 'w') as f:
        f.write(cm_py_file[1:])

    # Create colormap figure
    fig, ax = plt.subplots(frameon=False, figsize=(12.8, 3.2))
    fig.subplots_adjust(wspace=0)
    ax.imshow(rgb[np.newaxis, ...], aspect='auto')
    ax.set_axis_off()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.savefig("{0}/{0}.png".format(name), dpi=100, bbox_inches='tight',
                pad_inches=0)
    plt.close(fig)

    # Create txt-file with colormap data
    np.savetxt("cm_{0}.txt".format(name), rgb, fmt='%.8e')

    # Create txt-file with 8-bit colormap data
    rgb_8bit = np.rint(rgb*255)
    np.savetxt("{0}/{0}_8bit.txt".format(name), rgb_8bit, fmt='%i')

    # Load in all colormaps currently defined
    import_cmaps('.')

    # Make new colormap overview
    create_cmap_overview(savefig='cmap_overview.png', sort='lightness')
    create_cmap_overview(
        savefig=path.join(docs_dir, 'images', 'cmap_overview.png'),
        sort='lightness')
    create_cmap_overview(
        cmap_d.keys(), plot_profile=True, sort='lightness',
        savefig=path.join(docs_dir, 'images', 'mpl_cmaps.png'))

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
    if(cmtype == 'linear'):
        create_cmap_overview(
            cmap_cd['sequential'].values(), sort='lightness',
            savefig=path.join(docs_dir, 'images', 'seq_cmaps.png'))
        cmaps = [cm for cm in cmap_d if get_cmap_type(cm) == 'sequential']
        create_cmap_overview(
            cmaps, use_types=False,
            savefig=path.join(docs_dir, 'images', 'mpl_seq_cmaps.png'))
        cmtype = 'sequential'
    elif(cmtype == 'diverging'):
        create_cmap_overview(
            cmap_cd['diverging'].values(), sort='lightness',
            savefig=path.join(docs_dir, 'images', 'div_cmaps.png'))

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
