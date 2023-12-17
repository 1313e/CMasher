import sys

import tomli_w

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


with open("pyproject.toml", "rb") as fr:
    conf = tomllib.load(fr)

conf["project"]["dependencies"] = [
    req.replace(">=", "==") for req in conf["project"]["dependencies"]
]

with open("pyproject.toml", "wb") as fw:
    tomli_w.dump(conf, fw)
