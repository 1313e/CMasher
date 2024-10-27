import numpy as np
from matplotlib.legend_handler import HandlerBase


# Define legend handler class for artists that use colormaps
class _HandlerColorPolyCollection(HandlerBase):
    # Override create_artists to create an AxesImage resembling a colormap
    def create_artists(
        self, legend, artist, xdescent, ydescent, width, height, fontsize, trans
    ):
        from matplotlib.image import AxesImage

        # Obtain the Axes object of this legend
        ax = legend.axes

        # Obtain the colormap of the artist
        cmap = artist.cmap

        # Create an AxesImage to contain the colormap with proper dimensions
        image = AxesImage(
            ax, cmap=cmap, transform=trans, extent=[xdescent, width, ydescent, height]
        )

        # Set the data of the image
        image.set_data(np.arange(cmap.N)[np.newaxis, ...])

        # Return the AxesImage object
        return [image]
