.. _diverging:

Diverging colormaps
===================
A different category or class of colormaps, is the group of *diverging* colormaps.
Unlike sequential colormaps, diverging colormaps start at their lowest (or highest) lightness value at both ends and monotonically/linearly increase (decrease) to the highest (lowest) lightness value in the center.
They could be seen as two sequential colormaps combined together, that share the same lightness range and end/begin with the same color.
This makes them very useful to represent information that has a critical middle value or when data deviates around a common center (usually zero), like topographical maps; radial velocity plots or probability distributions.
The *matplotlib* package has quite a few diverging colormaps, but none of them starts and ends at the same lightness value; and most do not change perceptually uniform.
Therefore, a few alternatives are introduced here, with a full overview being shown below.

.. figure:: images/div_cmaps.png
    :width: 100%
    :align: center
    :alt: Overview of all diverging and cyclic colormaps in *CMasher* for Python.

    Overview of all diverging and cyclic colormaps in *CMasher*, sorted on lightness profile and perceptual range.
    The three numbers below the name of each colormap represent the central lightness value; the outer lightness value; and the perceptual range of that colormap, respectively.

.. _PRISM: https://github.com/1313e/PRISM

A special subcategory of diverging colormaps is the group of *cyclic* colormaps.
Cyclic colormaps are very similar to normal diverging colormaps, but instead of both sides only sharing one end with each other, the sides share both ends.
This means that the sides of a cyclic colormap both begin and end with the same color and thus theoretically speaking the colormap has no center.
While cyclic colormaps are significantly more niche than normal diverging colormaps due to this property, they are perfect for plotting information that is periodic in nature, like data affected by orientation and/or phase.
Due to the complexity and difficulty involved in creating proper cyclic colormaps, they tend to be quite rare, as *matplotlib* for example only has a single cyclic colormap, called *twilight*.
Because of this, *CMasher* provides a few cyclic colormaps of its own as well, which are shown in their separate category in the overview plot above.


.. toctree::
    :caption: Individual colormaps

    diverging/copper
    diverging/emergency
    diverging/fusion
    diverging/guppy
    diverging/holly
    diverging/iceburn
    diverging/infinity
    diverging/pride
    diverging/prinsenvlag
    diverging/redshift
    diverging/seasons
    diverging/seaweed
    diverging/viola
    diverging/waterlily
    diverging/watermelon
    diverging/wildfire
