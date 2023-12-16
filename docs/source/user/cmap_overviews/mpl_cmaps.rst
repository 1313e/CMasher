Full overview
=============
This colormap overview shows all colormaps in *matplotlib* and *CMasher*.
The colormaps are sorted on their type and lightness profile.
The individual lightness profiles are shown as well.
Note that perceptually uniform sequential colormaps should show no curves or changes in their lightness profile (except for diverging/cyclic colormaps, which have a single sharp transition in the center).

.. image:: ../images/mpl_cmaps.png
    :alt: Colormap overview of all colormaps in *matplotlib* and *CMasher*.
    :width: 100%
    :align: center

.. code:: python

    # Import packages
    import cmasher as cmr
    import matplotlib.pyplot as plt

    # Obtain list of all colormaps in MPL
    cmaps = plt.colormaps()

    # Create colormap overview of all colormaps in MPL
    cmr.create_cmap_overview(cmaps, plot_profile=True, sort='lightness')
