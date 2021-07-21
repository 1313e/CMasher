# -*- coding: utf-8 -*-

"""
CMasher Colormaps
=================
Holds all the different colormaps that are in *CMasher*.

"""


# %% IMPORTS
# Built-in imports
from typing import Dict

# Package imports
from matplotlib.colors import ListedColormap as LC

# All declaration
__all__ = []


# %% GLOBALS
# Type aliases
CMAP_DCT = Dict[str, LC]

# Initialize empty dict to hold colormaps in
cmap_d: CMAP_DCT = {}
cmap_cd: Dict[str, CMAP_DCT] = {
    'sequential': {},
    'diverging': {},
    'cyclic': {},
    'qualitative': {},
    'misc': {}}
