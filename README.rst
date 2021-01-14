|PyPI| |conda-forge| |Python| |Travis| |AppVeyor| |Coverage| |JOSS|

*CMasher*: Scientific colormaps for making accessible, informative and *cmashing* plots
=======================================================================================
The *CMasher* package provides a collection of scientific colormaps and utility functions to be used by different Python packages and projects, mainly in combination with `matplotlib`_, showcased in the `online documentation`_ (where I also describe how to use the colormaps in other languages).
The colormaps in *CMasher* are all designed to be perceptually uniform sequential using the `viscm`_ package; most of them are color-vision deficiency friendly; and they cover a wide range of different color combinations to accommodate for most applications.
It offers several alternatives to commonly used colormaps, like *chroma* and *rainforest* for *jet*; *sunburst* for *hot*; *neutral* for *binary*; and *fusion* and *redshift* for *coolwarm*.
If you cannot find your ideal colormap, then please open an `issue`_, provide the colors and/or style you want, and I will try to create one to your liking!
Let's get rid of all bad colormaps in the world together!

*If you use CMasher for your work, then please star the repo, such that I can keep track of how many users it has and more easily raise awareness of bad colormaps.*
*Additionally, if you use CMasher as part of your workflow in a scientific publication, please consider citing the CMasher paper* (*BibTeX:* ``cmr.get_bibtex``).

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

In the figure, one can see this wide range of color combinations that *CMasher* has to offer, as I wanted to make sure that *CMasher* has a colormap for everyone.
Because of this, *CMasher*'s sequential colormaps range from single major color maps like *amber*; *ember*; *flamingo*; *freeze*; *gothic*; and *jungle*, to colormaps with high perceptual ranges like *apple*; *chroma*; *heat*; *neon*; and *rainforest*.
The diverging colormaps in *CMasher* have a similar variety, but more importantly, several of them have a black center instead of a white center, like *iceburn*; *redshift*; *watermelon*; and *wildfire*.
Black centered diverging colormaps are quite rare as most researchers are used to white centered ones, even though a black centered diverging colormap can be rather useful in certain cases, like plotting a radial velocity map (the further away from the common center, the higher the velocity in either direction, and thus the corresponding color should be brighter).


Installation & Use
==================
How to install
--------------
*CMasher* can be easily installed directly from `PyPI`_ with::

    $ pip install cmasher

or from `conda-forge`_ with::

    $ conda install -c conda-forge cmasher  # If conda-forge is not set up as a channel
    $ conda install cmasher                 # If conda-forge is set up as a channel

If required, one can also clone the `repository`_ and install *CMasher* manually::

    $ git clone https://github.com/1313e/CMasher
    $ cd CMasher
    $ pip install .

*CMasher* can now be imported as a package with ``import cmasher as cmr``.

.. _repository: https://github.com/1313e/CMasher
.. _PyPI: https://pypi.org/project/CMasher
.. _conda-forge: https://anaconda.org/conda-forge/CMasher

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

For other use-cases, including an overview of *CMasher*'s utility functions and how to use *CMasher* in other programming languages, see the `online documentation`_.


.. |PyPI| image:: https://img.shields.io/pypi/v/CMasher.svg?logo=pypi&logoColor=white&label=PyPI
    :target: https://pypi.python.org/pypi/CMasher
    :alt: PyPI - Latest Release
.. |Python| image:: https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white
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
.. |JOSS| image:: https://img.shields.io/badge/JOSS-paper-brightgreen
   :target: https://doi.org/10.21105/joss.02004
   :alt: JOSS - Submission Status
.. |conda-forge| image:: https://img.shields.io/conda/vn/conda-forge/cmasher.svg?logo=conda-forge&logoColor=white
    :target: https://anaconda.org/conda-forge/cmasher
    :alt: Conda-Forge - Latest Release
