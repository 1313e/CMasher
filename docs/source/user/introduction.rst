.. _introduction:

Introduction
============
Description
-----------
The *CMasher* package provides a collection of scientific colormaps and utility functions to be used by different *Python* packages and projects, mainly in combination with `matplotlib`_ (see `here <https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html>`_ for an overview of all their colormaps as of v3.1.0).
The colormaps in *CMasher* are all designed to be perceptually uniform sequential using the `viscm`_ package; most of them are color-vision deficiency (CVD; color blindness) friendly; and they cover a wide range of different color combinations to accommodate for most applications.
It offers several alternatives to commonly used colormaps, like :ref:`chroma` and :ref:`rainforest` for *jet*; :ref:`sunburst` for *hot*; :ref:`neutral` for *binary*; and :ref:`fusion` and :ref:`redshift` for *coolwarm*.
If you cannot find your ideal colormap, then please open an `issue`_, provide the colors and/or style you want, and I will try to create one to your liking!

*If you use CMasher for your work, then please star the repo, such that I can keep track of how many users it has and more easily raise awareness of bad colormaps.*
*Additionally, if you use CMasher as part of your workflow in a scientific publication, please consider citing the CMasher paper* (*BibTeX:* :func:`~cmasher.get_bibtex`).

Colormap overview
-----------------
Below is an overview of all the colormaps that are currently in *CMasher* (made with the :func:`~cmasher.create_cmap_overview` function).

.. figure:: images/cmap_overview.png
    :width: 100%
    :align: center
    :alt: Overview of all colormaps in *CMasher* for Python.
    :name: cmr_cmaps

    Overview of all colormaps in *CMasher*.

In :numref:`cmr_cmaps`, one can see this wide range of color combinations that *CMasher* has to offer, as I wanted to make sure that *CMasher* has a colormap for everyone.
Because of this, *CMasher*'s sequential colormaps range from single major color maps like :ref:`amber`; :ref:`ember`; :ref:`flamingo`; :ref:`freeze`; :ref:`gothic`; and :ref:`jungle`, to colormaps with high perceptual ranges like :ref:`apple`; :ref:`chroma`; :ref:`torch`; :ref:`neon`; and :ref:`rainforest`.
The diverging colormaps in *CMasher* have a similar variety, but more importantly, several of them have a black center instead of a white center, like :ref:`iceburn`; :ref:`redshift`; :ref:`watermelon`; and :ref:`wildfire`.
Black centered diverging colormaps are quite rare as most researchers are used to white centered ones, even though a black centered diverging colormap can be rather useful in certain cases, like plotting a radial velocity map (the further away from the common center, the higher the velocity in either direction, and thus the corresponding color should be brighter).

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

*CMasher* can now be imported as a package with :pycode:`import cmasher as cmr`.

Besides *Python*, *CMasher*'s colormaps can also be accessed in various other languages and applications.
A list of all currently known languages and applications that support *CMasher* can be found in :ref:`accessing_colormaps`.

.. _example_use:

Example use
-----------
The colormaps shown above can be accessed by simply importing *CMasher*.
This makes them available in the :mod:`~cmasher` module, in addition to registering them in *matplotlib*'s :mod:`~matplotlib.cm` module (with added ``'cmr.'`` prefix to avoid name clashes).
So, for example, if one were to use the :ref:`rainforest` colormap, this could be done with::

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

See :ref:`usage` for more use-cases, including an overview of *CMasher*'s utility functions and how to use *CMasher* in other programming languages and applications.


.. _viscm: https://github.com/1313e/viscm
.. _repository: https://github.com/1313e/CMasher
.. _PyPI: https://pypi.org/project/CMasher
.. _conda-forge: https://anaconda.org/conda-forge/CMasher
.. _matplotlib: https://github.com/matplotlib/matplotlib
.. _issue: https://github.com/1313e/CMasher/issues
.. _cmasher/colormaps: https://github.com/1313e/CMasher/tree/master/src/cmasher/colormaps
