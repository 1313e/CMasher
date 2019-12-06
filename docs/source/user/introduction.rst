.. _introduction:

Introduction
============
The *CMasher* package provides a collection of scientific colormaps to be used by different *Python* packages and projects, mainly `matplotlib`_ (see `here <https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html>`_ for an overview of all their colormaps as of v3.1.0).
All colormaps presented here were made using the `viscm`_ package.
If you cannot find your ideal colormap, then please open an `issue`_, provide the colors and/or style you want, and I will try to create one to your liking!

Colormap overview
-----------------
Below is an overview of all the colormaps that are currently in *CMasher*.

.. image:: ../../../cmasher/colormaps/cmap_overview.png
    :width: 100%
    :align: center
    :alt: CMasher Colormap Overview

Example use
-----------
The colormaps shown above can be accessed by simply importing *CMasher* (which automatically executes the :func:`~cmasher.utils.import_cmaps` function on the ``cmasher/colormaps`` directory).
This makes them available in *CMasher*'s :mod:`~cmasher.cm` module, in addition to registering them in *matplotlib*'s :mod:`~matplotlib.cm` module (with added :pycode:`'cmr.'` prefix to avoid name clashes).
So, for example, if one were to use the *rainforest* colormap, this could be done with::

    # Import CMasher to register colormaps
    import cmasher as cmr

    # Import packages for plotting
    import matplotlib.pyplot as plt
    import numpy as np

    # Access rainforest colormap through CMasher
    cmap = cmr.rainforest

    # Access rainforest colormap through MPL
    # CMasher colormaps in MPL have an added 'cmr.' prefix
    cmap = 'cmr.rainforest'

    # Generate some data to plot
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = x**2+y**2

    # Make scatter plot of data with colormap
    plt.scatter(x, y, c=z, cmap=cmap, s=300)
    plt.show()

Accessing the colormaps in other packages than *matplotlib* would require reading in the text-files in the ``cmasher/colormaps`` directory, which contain the normalized RGB values (multiply by `255` for regular 8-bit values) of every colormap, and registering them in the package manually.
For those that are interested, the *viscm* source files that were used for creating the colormaps can be found in the `cmasher/colormaps`_ directory in the repo (the source files are not provided with the package distribution).

Background
----------
A good scientific colormap is often described/characterized as *perceptually uniform sequential*, which means that it is perceived as uniformly changing in lightness and saturation, mostly at the same hue.
This allows for the data values of a plot or image to be interpreted correctly by the viewer without giving false information (a great example of this can be found `here <https://mycarta.wordpress.com/2012/10/14/the-rainbow-is-deadlong-live-the-rainbow-part-4-cie-lab-heated-body/>`_), which could potentially even be dangerous.
It also often allows for a plot using a colormap to be converted properly to grey-scale without losing information.
Basically, when viewing a plot or image that uses color-coded values, it should be possible to infer how every color relates in terms of value to every other color, by simply looking at it (so, a legend or colorbar should NOT be necessary for this task).

Although this may sound easy enough, there are many colormaps out there that do this incorrectly.
The main problem usually is that humans do not perceive every color equally (for example, small variations in the color green are not perceived as it is such a natural color, while small variations in the colors red and blue are perceived).
Therefore, if one were to make a colormap that linearly increases in color wavelength, it would not be perceived as uniformly changing at all.
A good example of this is a colormap that is very commonly used in many different applications, the *jet* colormap:

.. figure:: images/jet_viscm.png
    :alt: Statistics of the *jet* colormap.
    :width: 100%
    :align: center
    :name: jet_viscm

    Output of the *viscm* package showing the statistics and performance of the *jet* colormap.
    The various different plots show how the colormap changes in lightness and perceived color, as well as how well the colormap converts to different types of color-vision deficiency (color blindness) and grey-scale.
    In case of a perceptually uniform sequential colormap, the two derivative plots should show a straight horizontal line; the colorspace diagram should be smooth; and the lines in the right-bottom corner plots should be visible up to the same depth across the entire colormap.

In :numref:`jet_viscm`, one can view the statistics output of the *jet* colormap, made with the `viscm`_ package.
As you can probably see, the *jet* colormap shows the spectrum of visible light, which trivially increases linearly in wavelength.
However, we can clearly see that this introduces multiple problems, as the color green for example is perceived as the brightest of the visible colors due to its very natural occurance.
This is an example of a colormap where it would be necessary to have a colorbar/legend, and it is overall a bad colormap to use.

These days, researchers are becoming more and more aware of what colormaps to use and what not, and of the fact that no single colormap can be used in all situations.
However, as there are still many more bad colormaps out there than good ones, it is going to take quite some time before they will disappear completely. 
For this reason, on this page, the different colormaps in *CMasher* are introduced and described what they should be used for, such that others can use them properly for their own projects.

.. _matplotlib: https://github.com/matplotlib/matplotlib
.. _viscm: https://github.com/matplotlib/viscm
.. _PRISM: https://github.com/1313e/PRISM
.. _issue: https://github.com/1313e/CMasher/issues
.. _cmasher/colormaps: https://github.com/1313e/CMasher/tree/master/cmasher/colormaps
