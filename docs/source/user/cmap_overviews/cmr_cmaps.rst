CMasher colormaps
=================
This colormap overview shows all colormaps in *CMasher*, as shown in :numref:`cmr_cmaps` on the :ref:`introduction` page.
The colormaps are sorted on their type and lightness profile.

.. image:: ../images/cmap_overview.png
    :alt: Colormap overview of all colormaps in *CMasher*.
    :width: 100%
    :align: center

.. code:: python

    # Import packages
    import cmasher as cmr

    # Create colormap overview of all colormaps in CMasher
    cmr.create_cmap_overview(sort='lightness')