# -*- coding: utf-8 -*-

# %% IMPORTS
# Future imports
from __future__ import absolute_import, division, print_function

# Built-in imports
import os
from os import path

# Package imports
from matplotlib import cm as mplcm
import pytest
from six import PY2

# CMasher imports
from cmasher import cm as cmrcm
from cmasher.utils import create_cmap_overview, import_cmaps

# Save the path to this directory
dirpath = path.dirname(__file__)


# %% PYTEST CLASSES AND FUNCTIONS
# Pytest class for create_cmap_overview
class Test_create_cmap_overview(object):
    # Test if default arguments work
    def test_default(self):
        create_cmap_overview()

    # Test if providing a custom list of colormaps works
    def test_list_no_types(self):
        create_cmap_overview([cmrcm.rainforest], use_types=0, sort='lightness')
        create_cmap_overview(['cmr.rainforest'], use_types=0, sort='lightness')

    # Test if providing a custom list of colormaps works
    def test_list_cat(self):
        create_cmap_overview(['cmr.rainforest'])

    # Test if providing all MPL colormap objects works
    def test_mpl_cmaps_objs(self):
        create_cmap_overview(mplcm.cmap_d.values(), sort='alphabetical')

    # Test if providing all MPL colormap names works
    def test_mpl_cmaps_names(self):
        create_cmap_overview(mplcm.cmap_d.keys(), sort='lightness')

    # Test if providing a custom dict of colormaps works
    def test_dict(self):
        create_cmap_overview({'test1': [cmrcm.rainforest],
                              'test2': ['cmr.rainforest']})

    # Test if the figure can be saved
    def test_savefig(self):
        create_cmap_overview(savefig="test.png")
        assert path.exists("./test.png")


# Pytest class for import_cmaps()-function
class Test_import_cmaps(object):
    # Test if providing a cmap .txt-file works
    def test_cmap_file_txt(self):
        import_cmaps(path.join(dirpath, '../colormaps/cm_rainforest.txt'))

    # Test if providing a cmap .jscm-file works (Py3) or errors (Py2)
    def test_cmap_file_jscm(self):
        if PY2:
            with pytest.raises(ValueError):
                import_cmaps(path.join(dirpath, 'data/cm_rainforest.jscm'))
        else:
            import_cmaps(path.join(dirpath, 'data/cm_rainforest.jscm'))

    # Test if all colormaps in cmasher/colormaps are loaded into MPL
    def test_MPL_cmaps(self):
        # Obtain path to directory with colormaps
        cmap_dir = path.abspath(path.join(dirpath, '../colormaps'))

        # Obtain list of all colormaps defined in CMasher
        # As all colormaps have their own directories, save them instead
        cm_names = next(os.walk(cmap_dir))[1]

        # Add the reversed versions to the list as well
        cm_names.extend([cm_name+'_r' for cm_name in cm_names])

        # Check if all names in cm_names are registered in CMasher and MPL
        for cm_name in cm_names:
            assert hasattr(cmrcm, cm_name)
            assert cm_name not in mplcm.cmap_d
            assert 'cmr.'+cm_name in mplcm.cmap_d

    # Test if providing a non-existing directory raises an error
    def test_non_existing_dir(self):
        with pytest.raises(OSError):
            import_cmaps('./test')

    # Test if providing an invalid cmap file raises an error
    def test_invalid_cmap_file(self):
        with pytest.raises(OSError):
            import_cmaps(path.join(dirpath, 'data/test.txt'))

    # Test if providing an invalid cmap .npy-file raises an error
    def test_invalid_cmap_npy_file(self):
        with pytest.raises(ValueError):
            import_cmaps(path.join(dirpath, 'data/cm_test2.npy'))

    # Test if providing a custom directory with invalid cmaps raises an error
    def test_invalid_cmap_dir(self):
        with pytest.raises(ValueError):
            import_cmaps(path.join(dirpath, 'data'))
