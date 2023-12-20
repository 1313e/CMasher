from pathlib import Path

import cmasher.cm as cmrcm
from cmasher._known_cmap_types import _CMASHER_BUILTIN_MAP_TYPES

HEADER = """from matplotlib.colors import ListedColormap as LC

CMAP_DCT = dict[str, LC]
cmap_d: CMAP_DCT
cmap_cd: dict[str, CMAP_DCT]

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
