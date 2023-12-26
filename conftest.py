# %% IMPORTS
# Built-in imports
import sys

# Package imports
import matplotlib as mpl
from py.path import local

# Set MPL backend
mpl.use("Agg")


# %% PYTEST CUSTOM CONFIGURATION PLUGINS
# This makes the pytest report header mention the tested CMasher version
def pytest_report_header(config):
    from cmasher.__version__ import __version__

    return "CMasher: %s" % (__version__)


def pytest_sessionstart(session):
    import cmasher

    global AT_START
    AT_START = set(mpl.colormaps.keys())


def pytest_sessionfinish(session, exitstatus):
    AT_END = set(mpl.colormaps.keys())
    if diff := (AT_END - AT_START):
        print(
            f"The following colormaps appear to have leaked during test session {diff}",
            file=sys.stderr,
        )


# %% PYTEST SETTINGS
# Set the current working directory to the temporary directory
local.get_temproot().chdir()
