"""
CMasher Colormaps
=================
Holds all the different colormaps that are in *CMasher*.

"""


# %% IMPORTS
# Built-in imports

# Package imports
from matplotlib.colors import ListedColormap as LC

# All declaration
__all__: list[str] = []


# %% GLOBALS
# Type aliases
CMAP_DCT = dict[str, LC]

# Initialize empty dict to hold colormaps in
cmap_d: CMAP_DCT = {}
cmap_cd: dict[str, CMAP_DCT] = {
    "sequential": {},
    "diverging": {},
    "cyclic": {},
    "qualitative": {},
    "misc": {},
}
