|PyPI| |Python| |Travis| |AppVeyor| |ReadTheDocs| |Coverage|

*CMasher*: Scientific colormaps for making accessible, informative and *cmashing* plots
=======================================================================================
The *CMasher* package provides a collection of scientific colormaps to be used by different *Python* packages and projects, mainly in combination with `matplotlib`_, showcased in the `online documentation`_.
The colormaps in *CMasher* are all designed to be perceptually uniform sequential using the `viscm`_ package; most of them are color-vision deficiency friendly; and they cover a wide range of different color combinations to accommodate for most applications.
It offers several alternatives to commonly used colormaps, like *chroma* and *rainforest* for *jet*; *sunburst* for *hot*; *neutral* for *binary*; and *fusion* and *redshift* for *coolwarm*.
If you cannot find your ideal colormap, then please open an `issue`_, provide the colors and/or style you want, and I will try to create one to your liking!
Let's get rid of all bad colormaps in the world together!

*If you use CMasher for your work, then please star the repo, such that I can keep track of how many users it has and more easily raise awareness of bad colormaps.*

.. _issue: https://github.com/1313e/CMasher/issues
.. _online documentation: https://cmasher.readthedocs.io
.. _matplotlib: https://github.com/matplotlib/matplotlib
.. _viscm: https://github.com/matplotlib/viscm

Colormap overview
-----------------
Below is an overview of all the colormaps that are currently in *CMasher* (made with the ``cmr.create_cmap_overview()`` function).
For more information, see the `online documentation`_.

.. image:: https://github.com/1313e/CMasher/raw/master/cmasher/colormaps/cmap_overview.png
    :width: 100%
    :align: center
    :target: https://cmasher.readthedocs.io
    :alt: CMasher Colormap Overview


Installation & Use
==================
How to install
--------------
*CMasher* can be found in the PyPI system, so ``pip install cmasher`` should suffice.

Example use
-----------
The colormaps shown above can be accessed by simply importing *CMasher*.
This makes them available in the ``cmasher`` module, in addition to registering them in *matplotlib*'s ``cm`` module (with added ``'cmr.'`` prefix to avoid name clashes).
So, for example, if one were to use the *rainforest* colormap, this could be done with:

.. code:: python

    # Import CMasher to register colormaps
    import cmasher as cmr

    # Import packages for plotting
    import matplotlib.pyplot as plt
    import numpy as np

    # Access rainforest colormap through CMasher or MPL
    cmap = cmr.rainforest                   # CMasher
    cmap = plt.get_cmap('cmr.rainforest')   # MPL

    # Generate some data to plot
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = x**2+y**2

    # Make scatter plot of data with colormap
    plt.scatter(x, y, c=z, cmap=cmap, s=300)
    plt.show()

Accessing the colormaps in other packages than *matplotlib* would require reading in the text files in the `cmasher/colormaps`_ directory, which contain the normalized RGB values (multiply by `255` for regular 8-bit values) of every colormap, and registering them in the package manually.
For those that are interested, the *viscm* source files that were used for creating the colormaps can also be found in the `cmasher/colormaps`_ directory in the repo (the source files are not provided with the package distribution).

Using custom colormaps
----------------------
*CMasher* allows for custom colormaps to be imported with the ``cmr.import_cmaps`` function (which is executed automatically on the `cmasher/colormaps`_ directory when *CMasher* is imported).
This function takes the path to a colormap file named ``cm_<cmap_name>`` (or the path to a directory containing such files); creates a *matplotlib* ``Colormap`` object using the data in the file; and registers it in *matplotlib* with the name ``'cmr.<cmap_name>'`` (it will also be available in the ``cmasher.cm`` module without the prefix).
A colormap file can either be a JSCM-file as created by *viscm* or a text file that contains the normalized RGB values of the colormap (see the text files in the `cmasher/colormaps`_ directory for the structure of such files).

Note that colormaps imported this way cannot be accessed through *CMasher* using ``cmr.<cmap_name>``, unlike *CMasher*'s own colormaps, but solely using ``cmr.cm.<cmap_name>`` (access through *matplotlib* is unchanged).
This is to keep official and unofficial colormaps separated in *CMasher*.

.. _cmasher/colormaps: https://github.com/1313e/CMasher/tree/master/cmasher/colormaps


.. |PyPI| image:: https://img.shields.io/pypi/v/CMasher.svg?logo=pypi&logoColor=white&label=PyPI
   :target: https://pypi.python.org/pypi/CMasher
   :alt: PyPI - Latest Release
.. |Python| image:: https://img.shields.io/pypi/pyversions/CMasher.svg?logo=python&logoColor=white&label=Python
   :target: https://pypi.python.org/pypi/CMasher
   :alt: PyPI - Python Versions
.. |Travis| image:: https://img.shields.io/travis/com/1313e/CMasher/master.svg?logo=travis%20ci&logoColor=white&label=Travis%20CI
   :target: https://travis-ci.com/1313e/CMasher
   :alt: Travis CI - Build Status
.. |AppVeyor| image:: https://img.shields.io/appveyor/ci/1313e/CMasher/master.svg?logo=appveyor&logoColor=white&label=AppVeyor
   :target: https://ci.appveyor.com/project/1313e/CMasher
   :alt: AppVeyor - Build Status
.. |ReadTheDocs| image:: https://img.shields.io/readthedocs/cmasher/latest.svg?logo=read%20the%20docs&logoColor=white&label=Docs
    :target: https://cmasher.readthedocs.io
    :alt: ReadTheDocs - Build Status
.. |Coverage| image:: https://img.shields.io/codecov/c/github/1313e/CMasher/master.svg?logo=codecov&logoColor=white&label=Coverage
    :target: https://codecov.io/gh/1313e/CMasher/branches/master
    :alt: CodeCov - Coverage Status
