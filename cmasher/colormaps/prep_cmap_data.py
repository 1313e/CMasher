# -*- coding: utf-8 -*-

# %% Imports
# Built-in imports
from importlib import import_module
import os
from os import path
import shutil
import sys
from textwrap import dedent

# Package imports
import matplotlib.pyplot as plt
import numpy as np
import viscm

# CMasher imports
from cmasher.cm import cmap_cd
from cmasher.utils import create_cmap_overview, import_cmaps


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
                                separator=', ', threshold=rgb.size)

    # Remove all whitespaces before commas
    for i in range(8, 0, -1):
        array_str = array_str.replace(' '*i+', ', '0'*i+', ')
        array_str = array_str.replace(' '*i+']', '0'*i+']')

    # Export as .py-file
    cm_py_file = dedent("""
        from matplotlib.colors import ListedColormap

        cm_type = "{0}"

        cm_data = {1}

        test_cm = ListedColormap(cm_data, name="{2}")
        """).format(cmtype, array_str, name)
    with open("{0}/{0}.py".format(name), 'w') as f:
        f.write(cm_py_file[1:])

    # Import created .py-file as a module
    # Functions as a test to see if it can be imported and accessed correctly
    cmap_mod = import_module("{0}.{0}".format(name))
    cmap = cmap_mod.test_cm

    # Create colormap figure
    x = np.linspace(0, 1, cmap.N)
    rgb = cmap(x)[:, :3]
    fig, ax = plt.subplots(frameon=False, figsize=(12.8, 3.2))
    fig.subplots_adjust(wspace=0)
    ax.imshow(rgb[np.newaxis, ...], aspect='auto')
    ax.set_axis_off()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.savefig("{0}/{0}.svg".format(name), dpi=100, bbox_inches='tight',
                pad_inches=0)
    plt.close(fig)

    # Create txt-file with colormap data
    np.savetxt("cm_{0}.txt".format(name), cmap_mod.cm_data)

    # Delete the created __pycache__ in the loaded cmap module
    shutil.rmtree("{0}/__pycache__".format(name), ignore_errors=True)

    # Load in all colormaps currently defined
    import_cmaps('.')

    # Make new colormap overview
    create_cmap_overview(savefig='cmap_overview.png', sort='lightness')
    create_cmap_overview(
        savefig='../../docs/source/user/images/cmap_overview.svg',
        sort='lightness')

    # Make new colormap type overviews
    if(cmtype == 'linear'):
        create_cmap_overview(
            cmap_cd['sequential'].values(), sort='lightness',
            savefig='../../docs/source/user/images/seq_cmaps.svg')
    elif(cmtype == 'diverging'):
        create_cmap_overview(
            cmap_cd['diverging'].values(), sort='lightness',
            savefig='../../docs/source/user/images/div_cmaps.svg')

    # Make string with the docs entry and print it
    docs_entry = dedent("""
        .. _{0}:

        {1}
        {2}
        .. image:: ../../../cmasher/colormaps/{0}/{0}.svg
            :alt: Visual representation of the *{0}* colormap.
            :width: 100%
            :align: center

        .. image:: ../../../cmasher/colormaps/{0}/{0}_viscm.svg
            :alt: Statistics of the *{0}* colormap.
            :width: 100%
            :align: center

        The *{0}* colormap is <visual representation>.
        <Lightness range><colors>
        <Recommended use>
        """).format(name, name.capitalize(), '-'*len(name))
    print(docs_entry)

    # Create viscm output figure
    viscm.gui.main(["view", "{0}/{0}.py".format(name), "--save",
                    "{0}/{0}_viscm.svg".format(name), "--quit"])
