Background
==========
A good scientific colormap is often described/characterized as *perceptually uniform sequential*, which means that it is perceived as uniformly changing in lightness and saturation, mostly at the same hue.
This allows for the data values of a plot to be interpreted correctly by the viewer without giving false information (a great example of this can be found `here <https://mycarta.wordpress.com/2012/10/14/the-rainbow-is-deadlong-live-the-rainbow-part-4-cie-lab-heated-body/>`_).
It also often allows for a plot to be converted properly to grey-scale without losing information.
Basically, it should be possible to infer how every color relates in terms of value to every other color, by simply looking at it (so, a legend or colorbar should NOT be necessary for this task).

Although this may sound easy enough, there are many colormaps out there that do this incorrectly.
The main problem usually is that humans do not perceive every color equally (e.g., small variations in the color green are not perceived as it is such a natural color, while small variations in the colors red and blue are perceived).
Therefore, if one were to make a colormap that linearly increases in color wavelength, it would not be perceived as uniformly changing at all.
A good example of this is a colormap that is very commonly used in many different applications, the *jet* colormap:

.. figure:: images/jet_viscm.png
    :alt: Statistics of the *jet* colormap.
    :width: 100%
    :align: center
    :name: jet_viscm

    Output of the *viscm* package showing the statistics and performance of the *jet* colormap.
    The various different plots show how the colormap changes in perceived color and lightness, as well as how well the colormap converts to different types of color-vision deficiency (color blindness) and grey-scale.
    In case of a perceptually uniform sequential colormap, the two derivative plots should show a straight horizontal line; the colorspace diagram should be smooth; and the lines in the right-bottom corner plots should be visible up to the same depth across the entire colormap.

In :numref:`jet_viscm`, one can view the statistics output of the *jet* colormap, made with the `viscm`_ package.
As you can probably see, the *jet* colormap shows the spectrum of visible light, which trivially increases linearly in wavelength.
However, we can clearly see that this introduces multiple problems, as the color green for example is perceived as the brightest of the visible colors due to its very natural occurance, and the colormap is absolutely not CVD-friendly.
This is an example of a colormap where it would be necessary to have a colorbar/legend, and it is overall a bad colormap to use.

Despite all of these problems, the *jet* colormap is still a very commonly used colormap.
An often cited reason for this (besides the general *"Everyone else uses it."*), is that *jet* has a high perceptual range, making it easier to distinguish adjacent values (it has a higher perceptual range than any colormap in *CMasher*, including the diverging colormaps).
Although this can be useful in many different cases, it certainly is not useful in all of them and there are ways to achieve this without giving false information.
In order to solve the problem of not knowing when to use what colormap, on the following pages, the different colormaps in *CMasher* are introduced and described what they should be used for, such that others can use them properly for their own projects.

.. _viscm: https://github.com/matplotlib/viscm
