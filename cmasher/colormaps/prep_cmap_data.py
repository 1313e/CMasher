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
from cmasher.utils import create_cmap_overview, import_cmaps


# %% MAIN SCRIPT
if(__name__ == '__main__'):
    # Check how many arguments were given
    if(len(sys.argv) == 2):
        # If only a single argument, then a sequential colormap is given
        jscm_path = path.abspath(sys.argv[1])
        name = path.splitext(path.basename(jscm_path))[0]

        # Make a directory for the colormap files
        os.mkdir(name)

        # Copy the .jscm-file to it
        shutil.move(jscm_path, name)

        # Load colormap from .jscm-file
        cmap = viscm.gui.Colormap(None, None, None)
        cmap.load("{0}/{0}.jscm".format(name))

        # Obtain RGB values of colormap
        v = viscm.viscm_editor(uniform_space=cmap.uniform_space,
                               cmtype=cmap.cmtype, method=cmap.method,
                               **cmap.params)
        rgb, _ = v.cmap_model.get_sRGB(num=256)
        cmtype = cmap.cmtype

    elif(len(sys.argv) == 3):
        # Else, a diverging colormap is provided
        jscm_paths = [path.abspath(arg) for arg in sys.argv[1:]]
        name = path.basename(path.commonprefix(jscm_paths))[:-1]

        # Make a directory for the colormap files
        os.mkdir(name)

        # Copy the .jscm-files to it
        for jscm_path in jscm_paths:
            shutil.move(jscm_path, name)

        # Load colormaps from .jscm-file
        cmap1 = viscm.gui.Colormap(None, None, None)
        cmap1.load("{0}/{1}".format(name, path.basename(jscm_paths[0])))
        cmap2 = viscm.gui.Colormap(None, None, None)
        cmap2.load("{0}/{1}".format(name, path.basename(jscm_paths[1])))

        # Obtain RGB values from both colormaps
        v1 = viscm.viscm_editor(uniform_space=cmap1.uniform_space,
                                cmtype=cmap1.cmtype, method=cmap1.method,
                                **cmap1.params)
        rgb1, _ = v1.cmap_model.get_sRGB(num=256)
        v2 = viscm.viscm_editor(uniform_space=cmap2.uniform_space,
                                cmtype=cmap2.cmtype, method=cmap2.method,
                                **cmap2.params)
        rgb2, _ = v2.cmap_model.get_sRGB(num=256)
        cmtype = cmap1.cmtype

        # Combine both RGB value lists into one
        rgb = np.concatenate([rgb1, rgb2[1:]], axis=0)

    # Export as .py-file
    array_list = np.array2string(rgb, max_line_width=79, prefix='cm_data = ',
                                 separator=', ', threshold=rgb.size)
    cm_py_file = dedent("""
        from matplotlib.colors import ListedColormap

        cm_type = "{0}"

        cm_data = {1}

        test_cm = ListedColormap(cm_data, name="{2}")
        """).format(cmtype, array_list, name)
    with open("{0}/{0}.py".format(name), 'w') as f:
        f.write(cm_py_file[1:])

    # Import created .py-file as a module
    # Functions as a test to see if it can be imported and accessed correctly
    cmap_mod = import_module("{0}.{0}".format(name))

    # Create colormap figure
    x = np.linspace(0, 1, 256)
    rgb = cmap_mod.test_cm(x)[np.newaxis, :, :3]
    fig, ax = plt.subplots(frameon=False, figsize=(12.8, 3.2))
    fig.subplots_adjust(wspace=0)
    ax.imshow(rgb, aspect='auto')
    ax.set_axis_off()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.savefig("{0}/{0}.png".format(name), dpi=200, bbox_inches='tight',
                pad_inches=0)
    plt.close(fig)

    # Create txt-file with colormap data
    np.savetxt("cm_{0}.txt".format(name), cmap_mod.cm_data)

    # Delete the created __pycache__ in the loaded cmap module
    shutil.rmtree("{0}/__pycache__".format(name), ignore_errors=True)

    # Load in all colormaps currently defined
    import_cmaps('.')

    # Make new colormap overview
    create_cmap_overview(savefig='cmap_overview.png')

    # Make string with the docs entry and print it
    docs_entry = dedent("""
        {0}
        {2}
        .. figure:: ../../../cmasher/colormaps/{1}/{1}.png
            :alt: Visual representation of the *{1}* colormap.
            :width: 100%
            :align: center
            :name: {1}_cmap

        .. figure:: ../../../cmasher/colormaps/{1}/{1}_viscm.png
            :alt: Statistics of the *{1}* colormap.
            :width: 100%
            :align: center
            :name: {1}_viscm

        The *{1}* colormap is <visual representation>.
        <Lightness range><colors>
        <Recommended use>
        """).format(name.capitalize(), name, '-'*len(name))
    print(docs_entry)

    # Create viscm output figure
    viscm.gui.main(["view", "{0}/{0}.py".format(name), "--save",
                    "{0}/{0}_viscm.png".format(name), "--quit"])
