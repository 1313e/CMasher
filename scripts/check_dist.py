# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
import sys
from pathlib import Path

import tomllib

REPO_DIR = Path(__file__).parents[1]
DIST_DIR = REPO_DIR / "dist"

with REPO_DIR.joinpath("pyproject.toml").open("rb") as fid:
    CMASHER_VERSION = tomllib.load(fid)["project"]["version"]

if __name__ == "__main__":
    if not DIST_DIR.exists():
        print("Did not find dist directory", file=sys.stderr)
        sys.exit(1)

    total_size = 0

    for root, _dirs, files in DIST_DIR.walk():
        for filename in files:
            if CMASHER_VERSION not in filename:
                continue
            if not filename.endswith((".tar.gz", ".whl")):
                continue
            total_size += root.joinpath(filename).stat().st_size

    print(f"total size: {total_size:_d} bytes", end=" ")
    print(f"({total_size/1024:.2f} kB)", end=" ")
    print(f"({total_size/(1024**2):.2f} MB)")

    if total_size / (1024**2) > 1:
        print("total size exceeds limit (1MB)", file=sys.stderr)
        sys.exit(1)
