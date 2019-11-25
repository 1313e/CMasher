# -*- coding: utf-8 -*-

"""
CMasher
========
Scientific colormaps for making stunning and *cmashing* plots.

"""


# %% IMPORTS AND DECLARATIONS
from __future__ import absolute_import, division, print_function

# CMasher imports
from .__version__ import __version__
from . import utils
from . import cm
from .cm import *

# All declaration
__all__ = ['cm', 'utils']
__all__.extend(cm.__all__)

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"
