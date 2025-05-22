from pathlib import Path

import cmasher.cm as cmrcm
from cmasher._known_cmap_types import _CMASHER_BUILTIN_MAP_TYPES

HEADER = """from matplotlib.colors import ListedColormap as LC

__all__: list[str]

CMAP_DCT = dict[str, LC]
cmap_d: CMAP_DCT
cmap_cd: dict[str, CMAP_DCT]

"""

"""
Python utility script designed to automatically generate a type hints interface (.pyi) file for the cmasher color map module. 
The script systematically creates type annotations for built-in color maps by iterating through `_CMASHER_BUILTIN_MAP_TYPES`, 
excluding color maps starting with \"cmr.\". It writes a type stub file with standard type hints for each color map and its reversed variant, 
enhancing type checking and IDE autocompletion support for the cmasher color map library. When executed, the script 
writes the type hints to a .pyi file located in the same directory as the cmasher color map module, providing a comprehensive 
type annotation interface for developers using the library.
"""

if __name__ == "__main__":
    pyi = Path(cmrcm.__file__).with_suffix(".pyi")

    with pyi.open("w", encoding="utf-8") as f:
        f.write(HEADER)

        for cmap in _CMASHER_BUILTIN_MAP_TYPES:
            if cmap.startswith("cmr."):
                continue

            f.write(f"{cmap}: LC\n")
            f.write(f"{cmap}_r: LC\n")
