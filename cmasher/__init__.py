"""
CMasher
=======
Scientific colormaps for making accessible, informative and *cmashing* plots.

"""


# %% IMPORTS AND DECLARATIONS
# CMasher imports
from .__version__ import __version__
from . import utils
from .utils import *
from . import cm
from .cm import *
from . import app_usage

# All declaration
__all__ = ['app_usage', 'cm', 'utils']
__all__.extend(cm.__all__)
__all__.extend(utils.__all__)

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"
