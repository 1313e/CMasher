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
from matplotlib import cm as mplcm
from matplotlib.colors import LinearSegmentedColormap as LSC
import numpy as np

# CMasher imports
from cmasher import cm

# All declaration
__all__ = ['import_cmaps']


# %% FUNCTIONS
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
            cmap = LSC.from_list(cm_name, colorlist, N=len(colorlist))
            cmap_r = LSC.from_list(cm_name+'_r', list(reversed(colorlist)),
                                   N=len(colorlist))

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
