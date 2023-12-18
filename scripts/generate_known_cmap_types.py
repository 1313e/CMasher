# run this script to regenerate cmasher._known_cmap_types
import re
from pathlib import Path

LINE_REGEXP = re.compile(r'cm_type = "(?P<name>[\w_]+)"\n')
DIR = Path(__file__).parents[1] / "cmasher" / "colormaps"

res = {}
for sdir in DIR.glob("*"):
    if not sdir.is_dir():
        continue
    for file in sdir.glob("*.py"):
        name = file.stem
        with open(file) as fh:
            while line := fh.readline():
                if (match := LINE_REGEXP.fullmatch(line)) is not None:
                    res[f"{name}"] = match.group("name")
                    res[f"cmr.{name}"] = match.group("name")
                    continue

THIS_SCRIPT = Path(__file__).name
with open(DIR.parent / "_known_cmap_types.py", "w") as fh:
    fh.write(
        f"# this file is generated via scripts/{THIS_SCRIPT}, do not edit manually\n\n"
    )

    fh.write("_CMASHER_BUILTIN_MAP_TYPES = {\n")
    for name, val in dict(sorted(res.items())).items():
        fh.write(f'    "{name}": "{val}",\n')
    fh.write("}\n")
