import sys

import matplotlib as mpl
import pytest
from py.path import local

# Set MPL backend
mpl.use("Agg")


# %% PYTEST CUSTOM CONFIGURATION PLUGINS
# This makes the pytest report header mention the tested CMasher version
def pytest_report_header(config):
    from cmasher.__version__ import __version__

    return f"CMasher: {__version__}"


def pytest_sessionstart(session):
    import cmasher

    global AT_START
    AT_START = set(mpl.colormaps.keys())


def pytest_sessionfinish(session, exitstatus):
    AT_END = set(mpl.colormaps.keys())
    if diff := (AT_END - AT_START):  # pragma: no cover
        print(
            f"The following colormaps appear to have leaked during test session {diff}",
            file=sys.stderr,
        )


# %% PYTEST SETTINGS
# Set the current working directory to the temporary directory
local.get_temproot().chdir()


# %% FIXTURES
@pytest.fixture(scope="function", autouse=True)
def clean_registration():
    old = set(mpl.colormaps.keys())
    yield
    new = set(mpl.colormaps.keys())
    for name in new - old:
        if mpl.__version_info__ >= (3, 6):
            mpl.colormaps.unregister(name)
        else:
            mpl.cm.unregister_cmap(name)
