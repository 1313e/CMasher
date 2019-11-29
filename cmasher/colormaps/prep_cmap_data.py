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
    # Define name of colormap
    jscm_path = path.abspath(sys.argv[1])
    name = path.splitext(path.basename(jscm_path))[0]

    # Make a directory for the colormap files
    os.mkdir(name)

    # Copy the .jscm-file to it
    shutil.move(jscm_path, name)

    # Load colormap from .jscm-file
    cmap = viscm.gui.Colormap(None, None, None)
    cmap.load("{0}/{0}.jscm".format(name))

    # Export as .py-file
    v = viscm.viscm_editor(uniform_space=cmap.uniform_space,
                           cmtype=cmap.cmtype, method=cmap.method,
                           **cmap.params)
    rgb, _ = v.cmap_model.get_sRGB(num=256)
    array_list = np.array2string(rgb, max_line_width=79, prefix='cm_data = ',
                                 separator=', ', threshold=rgb.size)
    cm_py_file = dedent("""
        from matplotlib.colors import ListedColormap

        cm_type = "{0}"

        cm_data = {1}
        test_cm = ListedColormap(cm_data, name="{2}")
        """).format(v.cmtype, array_list, name)
    with open("{0}/{0}.py".format(name), 'w') as f:
        f.write(cm_py_file)

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

    # Create viscm output figure
    viscm.gui.main(["view", "{0}/{0}.py".format(name), "--save",
                    "{0}/{0}_viscm.png".format(name), "--quit"])
