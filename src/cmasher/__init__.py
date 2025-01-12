"""
CMasher
=======
Scientific colormaps for making accessible, informative and *cmashing* plots.

"""

from . import app_usage, cm, utils
from .__version__ import __version__
from .cm import *
from .utils import *

# All declaration
__all__ = ["app_usage", "cm", "utils"]
__all__.extend(cm.__all__)
__all__.extend(utils.__all__)

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"
