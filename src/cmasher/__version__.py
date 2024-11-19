"""
CMasher Version
===============
Stores the different versions of the *CMasher* package.

"""

# %% VERSIONS
# Default/Latest/Current version
from importlib.metadata import version

__version__ = version("cmasher")
del version
