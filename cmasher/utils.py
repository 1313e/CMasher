# -*- coding: utf-8 -*-

"""
Utils
=====
Utility functions required for registering all defined scientific colormaps.

"""


# %% IMPORTS
# Future imports
from __future__ import absolute_import, division, print_function

# Built-in imports
import os
from os import path

# Package imports
from colorspacious import cspace_converter
from matplotlib import cm as mplcm
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

# CMasher imports
from cmasher import cm

# All declaration
__all__ = ['create_cmap_overview', 'import_cmaps']


# %% FUNCTIONS
# This function creates an overview plot of all colormaps specified
def create_cmap_overview(cmap_list=None, savefig=None):
    """
    Creates an overview plot containing all colormaps defined in the provided
    `cmap_list`.

    Optional
    --------
    cmap_list : list of str or None. Default: None
        A list of all colormap names that must be included in the overview
        plot. If *None*, all colormaps defined in *CMasher* are used instead.
    savefig : str or None. Default: None
        If not *None*, the path to where the overview plot must be saved to.
        Else, the plot will simply be shown.

    """

    # If cmap_list is None, use cmap_d.keys
    if cmap_list is None:
        cmap_list = cm.cmap_d.keys()

    # Remove any reversed versions
    cmap_list = [cmap for cmap in cmap_list if not cmap.endswith('_r')]
    cmap_list.sort()

    # Obtain the colorspace converter for showing cmaps in grey-scale
    cspace_convert = cspace_converter("sRGB1", "CAM02-UCS")

    # Create figure instance
    height = 0.4*(len(cmap_list)+1)
    fig, axes = plt.subplots(figsize=(6.4, height),
                             nrows=len(cmap_list), ncols=2)
    w_pad, h_pad, wspace, hspace = fig.get_constrained_layout_pads()
    fig.subplots_adjust(top=(1-0.24/height), bottom=0.01, left=0.2, right=0.99,
                        wspace=0.05)
    fig.suptitle("Colormap Overview", fontsize=14, y=1.0, x=0.6)

    # If cmap_list only has a single element, make sure axes is a list
    if(len(cmap_list) == 1):
        axes = [axes]

    # Loop over all cmaps defined in cmap list
    for ax, cmap in zip(axes, cmap_list):
        # Get the colormap
        cmap = mplcm.get_cmap(cmap)

        # Get array of all values for which a colormap value is requested
        x = np.linspace(0, 1, cmap.N)

        # Get RGB values for colormap.
        rgb = cmap(x)[np.newaxis, :, :3]

        # Get lightness values of cmap
        lab = cspace_convert(rgb)
        L = lab[0, :, 0]

        # Get corresponding RGB values for lightness values using cm.neutral
        rgb_L = cm.neutral(L/99.99871678)[np.newaxis, :, :3]

        # Add subplots
        ax[0].imshow(rgb, aspect='auto')
        ax[0].set_axis_off()
        ax[1].imshow(rgb_L, aspect='auto')
        ax[1].set_axis_off()
        pos = list(ax[0].get_position().bounds)
        x_text = pos[0]-0.01
        y_text = pos[1]+pos[3]/2
        fig.text(x_text, y_text, cmap.name, va='center', ha='right',
                 fontsize=10)

    # If savefig is not None, save the figure
    if savefig is not None:
        plt.savefig(savefig, dpi=250)
        plt.close(fig)
    # Else, simply show it
    else:
        plt.show()


# Function to import all custom colormaps in a file or directory
def import_cmaps(cmap_path):
    """
    Reads in custom colormaps from a provided file or directory `cmap_path`,
    transforms them into :obj:`~matplotlib.colors.LinearSegmentedColormap`
    objects and registers them in the :mod:`matplotlib.cm` and
    :mod:`cmasher.cm` modules. Both the imported colormap and its reversed
    version will be registered.

    Parameters
    ----------
    cmap_path : str
        Relative or absolute path to a custom colormap file or directory that
        contains custom colormap files. A colormap file can be a NumPy binary
        file ('.npy' or '.npz') or any text file.

    Notes
    -----
    All colormap files must have names starting with 'cm\\_'. The resulting
    colormaps will have the name of their file without the prefix and
    extension.

    """

    # Obtain path to file or directory with colormaps
    cmap_path = path.abspath(cmap_path)

    # Check if provided file or directory exists
    if not path.exists(cmap_path):
        raise OSError("Input argument 'cmap_path' is a non-existing path (%r)!"
                      % (cmap_path))

    # Check if cmap_path is a file or directory and act accordingly
    if path.isfile(cmap_path):
        # If file, split cmap_path up into dir and file components
        cmap_dir, cmap_file = path.split(cmap_path)

        # Check if its name starts with 'cm_' and raise error if not
        if(cmap_file[:3] != 'cm_'):
            raise OSError("Input argument 'cmap_path' does not lead to a file "
                          "with the 'cm_' prefix (%r)!" % (cmap_path))

        # Set cm_files to be the sole read-in file
        cm_files = [cmap_file]
    else:
        # If directory, obtain the names of all files in cmap_path
        cmap_dir = cmap_path
        filenames = next(os.walk(cmap_dir))[2]

        # Extract the files with defined colormaps
        cm_files = [name for name in filenames if name[:3] == 'cm_']
        cm_files.sort()

    # Read in all the defined colormaps, transform and register them
    for cm_file in cm_files:
        # Split basename and extension
        base_str, ext_str = path.splitext(cm_file)
        cm_name = base_str[3:]

        # Process colormap files
        try:
            # Obtain absolute path to colormap data file
            cm_file_path = path.join(cmap_dir, cm_file)

            # Read in colormap data
            if ext_str in ('.npy', '.npz'):
                # If file is a NumPy binary file
                colorlist = np.load(cm_file_path).tolist()
            else:
                # If file is anything else
                colorlist = np.genfromtxt(cm_file_path).tolist()

            # Transform colorlist into a Colormap
            cmap = ListedColormap(colorlist, cm_name, N=len(colorlist))
            cmap_r = cmap.reversed()

            # Test that the colormaps can be called
            cmap(1)
            cmap_r(1)

            # Add cmap to matplotlib's cmap list
            mplcm.register_cmap(cmap=cmap)
            setattr(cm, cm_name, cmap)
            cm.__all__.append(cm_name)
            cm.cmap_d[cm_name] = cmap

            # Add reversed cmap to matplotlib's cmap list
            mplcm.register_cmap(cmap=cmap_r)
            setattr(cm, cm_name+'_r', cmap_r)
            cm.__all__.append(cm_name+'_r')
            cm.cmap_d[cm_name+'_r'] = cmap_r
        except Exception as error:
            raise ValueError("Provided colormap %r is invalid! (%s)"
                             % (cm_name, error))


# Import all colormaps defined in './colormaps'
import_cmaps(path.join(path.dirname(__file__), 'colormaps'))
