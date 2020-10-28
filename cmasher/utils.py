# -*- coding: utf-8 -*-

"""
Utils
=====
Utility functions for registering and manipulating colormaps in various ways.

"""


# %% IMPORTS
# Built-in imports
from collections import OrderedDict as odict
from glob import glob
from os import path
from textwrap import dedent

# Package imports
from colorspacious import cspace_converter
from matplotlib import cm as mplcm
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap as LC, to_hex, to_rgb
from matplotlib.legend import Legend
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import AxesImage
import matplotlib.pyplot as plt
import numpy as np

# CMasher imports
from cmasher import cm as cmrcm

# All declaration
__all__ = ['create_cmap_mod', 'create_cmap_overview', 'get_bibtex',
           'get_cmap_type', 'get_sub_cmap', 'import_cmaps', 'register_cmap',
           'set_cmap_legend_entry', 'take_cmap_colors']


# %% HELPER CLASSES
# Define legend handler class for artists that use colormaps
class _HandlerColorPolyCollection(HandlerBase):
    # Override create_artists to create an AxesImage resembling a colormap
    def create_artists(self, legend, artist, xdescent, ydescent, width, height,
                       fontsize, trans):
        # Obtain the Axes object of this legend
        ax = legend.axes

        # Obtain the colormap of the artist
        cmap = artist.cmap

        # Create an AxesImage to contain the colormap with proper dimensions
        image = AxesImage(ax, cmap=cmap, transform=trans,
                          extent=[xdescent, width, ydescent, height])

        # Set the data of the image
        image.set_data(np.arange(cmap.N)[np.newaxis, ...])

        # Return the AxesImage object
        return([image])


# %% HELPER FUNCTIONS
# Define function for obtaining the sorting order for lightness ranking
def _get_cmap_lightness_rank(cmap):
    """
    Returns a tuple of objects used for sorting the provided `cmap` based
    on its lightness profile.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    L_type : int
        The type of lightness profile of `cmap`.
        This is only used for sequential colormaps.
    L_start : float
        The starting lightness value of `cmap`.
        For diverging colormaps, this is the central lightness value.
    L_rng : float
        The lightness range (L_max-L_min) of `cmap`.
    L_rmse : float
        The RMSE of the lightness profile of `cmap`.
        For diverging colormaps, this is the max RMSE of either half.
    name : str
        The name of `cmap`.
        For qualitative and miscellaneous colormaps, this is the only value
        that is used.

    """

    # Obtain the colormap
    cmap = mplcm.get_cmap(cmap)

    # Get RGB values for colormap
    rgb = cmap(np.arange(cmap.N))[:, :3]

    # Get lightness values of colormap
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    L = lab[:, 0]

    # Determine the deltas of the lightness profile
    deltas = np.diff(L)
    derivs = (cmap.N-1)*deltas

    # Set lightness profile type to 0
    L_type = 0

    # Determine the RMSE of the lightness profile of a sequential colormap
    if(get_cmap_type(cmap) == 'sequential'):
        # Take RMSE of entire lightness profile
        L_rmse = np.around(np.std(derivs), 1)

        # Calculate starting lightness value
        L_start = np.around(L[0], 1)

        # Determine type of lightness profile
        L_type += ~(np.sum(rgb[0]) == 0)*2
        L_type += ((np.sum(rgb[0]) == 0) == (np.sum(rgb[-1]) == 3))

    # Diverging/cyclic colormaps
    elif get_cmap_type(cmap) in ('diverging', 'cyclic'):
        # Calculate RMSE of both halves
        central_i = [int(np.floor(cmap.N/2)), int(np.ceil(cmap.N/2))]
        L_rmse = np.max([np.around(np.std(derivs[:central_i[0]]), 1),
                         np.around(np.std(derivs[central_i[1]:]), 1)])

        # Calculate central lightness value
        L_start = np.around(np.average(L[central_i]), 1)

    # Determine lightness range for sequential/diverging/cyclic colormaps
    if get_cmap_type(cmap) in ('sequential', 'diverging', 'cyclic'):
        L_min = np.around(np.min(L), 1)
        L_max = np.around(np.max(L), 1)
        L_rng = np.around(np.abs(L_max-L_min), 1)

    # For qualitative/misc colormaps, set all lightness values to zero
    else:
        L_type = L_start = L_rng = L_rmse = 0

    # Return lightness contributions to the rank
    return(L_type, L_start, L_rng, L_rmse, cmap.name)


# %% FUNCTIONS
# This function creates a standalone module of a CMasher colormap
def create_cmap_mod(cmap, *, save_dir='.'):
    """
    Creates a standalone Python module of the provided *CMasher* `cmap` and
    saves it in the given `save_dir` as '<`cmap`>.py'.

    A standalone colormap module can be used to quickly share a colormap with
    someone without adding the *CMasher* dependency.
    Importing the created module allows the colormap to be used in the same way
    as usual through *MPL* (including the 'cmr.' prefix).

    Parameters
    ----------
    cmap : str
        The name of the *CMasher* colormap a standalone Python module must be
        made for. An added 'cmr.' prefix will be ignored.

    Optional
    --------
    save_dir : str. Default: '.'
        The path to the directory where the module must be saved.
        By default, the current directory is used.

    Returns
    -------
    cmap_path : str
        The path to the Python file containing the colormap module.

    Example
    -------
    Creating a standalone Python module of the 'rainforest' colormap::

        >>> create_cmap_mod('rainforest')

    One can now import the 'rainforest' colormap in any script by moving the
    created 'rainforest.py' file to the proper working directory and importing
    it with ``import rainforest``.

    Note
    ----
    Unlike other *CMasher* utility functions, `cmap` solely accepts names of
    colormaps that are registered in *CMasher* (:mod:`cmasher.cm`).

    """

    # Get absolute value to provided save_dir
    save_dir = path.abspath(save_dir)

    # Remove any 'cmr.' prefix from provided cmap
    name = cmap.replace('cmr.', '')

    # Obtain the CMasher colormap associated with the provided cmap
    cmap = cmrcm.cmap_d.get(name, None)

    # If cmap is None, raise error
    if cmap is None:
        raise ValueError("Input argument 'cmap' is not a valid CMasher "
                         "colormap (%r)!" % (name))

    # Obtain the RGB tuples of provided cmap
    rgb = np.array(cmap.colors)

    # Convert RGB values to string
    array_str = np.array2string(rgb, max_line_width=79, prefix='cm_data = ',
                                separator=', ', threshold=rgb.size,
                                formatter={'float': lambda x: "%.8f" % (x)})

    # Create Python module template and add obtained RGB data to it
    cm_py_file = dedent("""
        # %% IMPORTS
        # Package imports
        from matplotlib.cm import register_cmap
        from matplotlib.colors import ListedColormap

        # All declaration
        __all__ = ['cmap']

        # Author declaration
        __author__ = "Ellert van der Velden (@1313e)"

        # Package declaration
        __package__ = 'cmasher'


        # %% GLOBALS AND DEFINITIONS
        # Type of this colormap
        cm_type = '{0}'

        # RGB-values of this colormap
        cm_data = {1}

        # Create ListedColormap object for this colormap
        cmap = ListedColormap(cm_data, name='cmr.{2}', N=len(cm_data))
        cmap_r = cmap.reversed()

        # Register (reversed) cmap in MPL
        register_cmap(cmap=cmap)
        register_cmap(cmap=cmap_r)
        """).format(get_cmap_type(cmap), array_str, name)

    # Obtain the path to the module
    cmap_path = path.join(save_dir, "{0}.py".format(name))

    # Create Python module
    with open(cmap_path, 'w') as f:
        f.write(cm_py_file[1:])

    # Return cmap_path
    return(cmap_path)


# This function creates an overview plot of all colormaps specified
def create_cmap_overview(cmaps=None, *, savefig=None, use_types=True,
                         sort='alphabetical', plot_profile=False,
                         title="Colormap Overview"):
    """
    Creates an overview plot containing all colormaps defined in the provided
    `cmaps`.

    Optional
    --------
    cmaps : list of {str; :obj:`~matplotlib.colors.Colormap` objects}, dict \
        of lists or None. Default: None
        A list of all colormaps that must be included in the overview plot.
        If dict of lists, the keys define categories for the colormaps.
        If *None*, all colormaps defined in *CMasher* are used instead.
    savefig : str or None. Default: None
        If not *None*, the path where the overview plot must be saved to.
        Else, the plot will simply be shown.
    use_types : bool. Default: True
        Whether all colormaps in `cmaps` should be categorized into their
        colormap types (sequential; diverging; cyclic; qualitative; misc).
        If `cmaps` is a dict, this value is ignored.
    sort : {'alphabetical'/'name'; 'lightness'}, function or None. Default: \
        'alphabetical'
        String or function indicating how the colormaps should be sorted in the
        overview.
        If 'alphabetical', the colormaps are sorted alphabetically on their
        name.
        If 'lightness', the colormaps are sorted based on their lightness
        profile.
        If function, a function definition that takes a
        :obj:`~matplotlib.colors.Colormap` object and returns the sorted
        position of that colormap.
        If *None*, the colormaps retain the order they were given in.
    plot_profile : bool or float. Default: False
        Whether the lightness profiles of all colormaps should be plotted. If
        not *False*, the lightness profile of a colormap is plotted on top of
        its gray-scale version and `plot_profile` is used for setting the alpha
        (opacity) value.
        If `plot_profile` is *True*, it will be set to `0.25`.
    title : str or None. Default: "Colormap Overview"
        String to be used as the title of the colormap overview.
        If empty or *None*, no title will be used.

    Notes
    -----
    The colormaps in `cmaps` can either be provided as their registered name in
    :mod:`matplotlib.cm`, or their corresponding
    :obj:`~matplotlib.colors.Colormap` object.
    Any provided reversed colormaps (colormaps that end their name with '_r')
    are ignored if their normal versions were provided as well.

    If `plot_profile` is not set to *False*, the lightness profiles are plotted
    on top of the gray-scale colormap versions, where the y-axis ranges from 0%
    lightness to 100% lightness.
    The lightness profile transitions between black and white at 50% lightness.

    """

    # If plot_profile is True, set it to its default value
    if plot_profile is True:
        plot_profile = 0.25

    # If cmaps is None, use cmap_d.values
    if cmaps is None:
        cmaps = cmrcm.cmap_d.values()

    # If sort is a string, obtain proper function
    if isinstance(sort, str):
        # Convert sort to lowercase
        sort = sort.lower()

        # Check what string was provided and obtain sorting function
        if sort in ('alphabetical', 'name'):
            def sort(x):
                return(x.name)
        elif(sort == 'lightness'):
            sort = _get_cmap_lightness_rank

    # Create empty list of cmaps
    cmaps_list = []

    # If cmaps is a dict, it has cm_types defined
    if isinstance(cmaps, dict):
        # Set use_types to True
        use_types = True

        # Define empty dict of colormaps
        cmaps_dict = odict()

        # Save provided cmaps as something else
        input_cmaps = cmaps

        # Loop over all cm_types
        for cm_type, cmaps in input_cmaps.items():
            # Add empty list of colormaps to cmaps_dict with this cm_type
            cmaps_dict[cm_type] = []

            # Loop over all cmaps and remove reversed versions
            for cmap in cmaps:
                if isinstance(cmap, str):
                    cmaps_dict[cm_type].append(mplcm.get_cmap(cmap))
                else:
                    cmaps_dict[cm_type].append(cmap)

    # Else, it is a list with no cm_types
    else:
        # If cm_types are requested
        if use_types:
            # Define empty dict with the base cm_types
            cm_types = ['sequential', 'diverging', 'cyclic', 'qualitative',
                        'misc']
            cmaps_dict = odict([[cm_type, []] for cm_type in cm_types])

            # Loop over all cmaps and remove reversed versions
            for cmap in cmaps:
                cm_type = get_cmap_type(cmap)
                if isinstance(cmap, str):
                    cmaps_dict[cm_type].append(mplcm.get_cmap(cmap))
                else:
                    cmaps_dict[cm_type].append(cmap)
        else:
            # Loop over all cmaps and remove reversed versions
            for cmap in cmaps:
                if isinstance(cmap, str):
                    cmaps_list.append(mplcm.get_cmap(cmap))
                else:
                    cmaps_list.append(cmap)

    # If use_types is True, a dict is currently used
    if use_types:
        # Convert entire cmaps_dict into a list again
        for key, value in cmaps_dict.items():
            # If this cm_type has at least 1 colormap, sort and add them
            if value:
                # Obtain the names of all colormaps
                names = [x.name for x in value]

                # Remove all reversed colormaps that also have their original
                off_dex = len(names)-1
                for i, name in enumerate(reversed(names)):
                    if name.endswith('_r') and name[:-2] in names:
                        value.pop(off_dex-i)

                # Sort the colormaps if requested
                if sort is not None:
                    value.sort(key=sort)

                # Add to list
                cmaps_list.append((key, False))
                cmaps_list.extend(value)

    # Else, a list is used
    else:
        # Obtain the names of all colormaps
        names = [x.name for x in cmaps_list]

        # Remove all reversed colormaps that also have their original
        off_dex = len(names)-1
        for i, name in enumerate(reversed(names)):
            if name.endswith('_r') and name[:-2] in names:
                cmaps_list.pop(off_dex-i)

        # Sort the colormaps if requested
        if sort is not None:
            cmaps_list.sort(key=sort)

    # Add title to cmaps_list if requested
    if title:
        cmaps_list.insert(0, (title, True))

    # Obtain the colorspace converter for showing cmaps in grey-scale
    cspace_convert = cspace_converter("sRGB1", "CAM02-UCS")

    # Create figure instance
    height = 0.4*len(cmaps_list)+0.1
    fig, axs = plt.subplots(figsize=(6.4, height), nrows=len(cmaps_list),
                            ncols=2)

    # Adjust subplot positioning
    fig.subplots_adjust(top=(1-0.05/height), bottom=0.05/height, left=0.2,
                        right=0.99, wspace=0.05)

    # If cmaps_list only has a single element, make sure axs is a list
    if(len(cmaps_list) == 1):
        axs = [axs]

    # Loop over all cmaps defined in cmaps list
    for (ax0, ax1), cmap in zip(axs, cmaps_list):
        # Turn axes off
        ax0.set_axis_off()
        ax1.set_axis_off()

        # Obtain position bbox of ax0
        pos0 = ax0.get_position()

        # If cmap is a tuple, it defines a title or cm_type
        if isinstance(cmap, tuple):
            # If it is a title
            if cmap[1]:
                # Write the title as text in the correct position
                fig.text(0.595, pos0.y0+pos0.height/2, cmap[0],
                         va='center', ha='center', fontsize=18)

            # If it is a cm_type
            else:
                # Write the cm_type as text in the correct position
                fig.text(0.595, pos0.y0, cmap[0],
                         va='bottom', ha='center', fontsize=14)

        # Else, this is a colormap
        else:
            # Obtain the colormap type
            cm_type = get_cmap_type(cmap)

            # Get array of all values for which a colormap value is requested
            x = np.arange(cmap.N)

            # Get RGB values for colormap
            rgb = cmap(x)[:, :3]

            # Get lightness values of colormap
            lab = cspace_convert(rgb)
            L = lab[:, 0]

            # Normalize lightness values
            L /= 99.99871678

            # Get corresponding RGB values for lightness values using neutral
            rgb_L = cmrcm.neutral(L)[:, :3]

            # Add colormap subplot
            ax0.imshow(rgb[np.newaxis, ...], aspect='auto')

            # Check if the lightness profile was requested
            if plot_profile and (cm_type != 'qualitative'):
                # Determine the points that need to be plotted
                plot_L = -(L-0.5)
                points = np.stack([x, plot_L], axis=1)

                # Determine the colors that each point must have
                # Use black for L >= 0.5 and white for L <= 0.5.
                colors = np.zeros_like(plot_L, dtype=int)
                colors[plot_L >= 0] = 1

                # Split points up into segments with the same color
                s_idx = np.nonzero(np.diff(colors))[0]+1
                segments = np.split(points, s_idx)

                # Loop over all pairs of adjacent segments
                for i, (seg1, seg2) in enumerate(zip(segments[:-1],
                                                     segments[1:])):
                    # Determine the point in the center of these segments
                    central_point = (seg1[-1]+seg2[0])/2

                    # Add this point to the ends of these segments
                    # This ensures that the color changes in between segments
                    segments[i] = np.concatenate(
                        [segments[i], [central_point]], axis=0)
                    segments[i+1] = np.concatenate(
                        [[central_point], segments[i+1]], axis=0)

                # Create an MPL LineCollection object with these segments
                lc = LineCollection(segments, cmap=cmrcm.neutral,
                                    alpha=plot_profile)
                lc.set_linewidth(1)

                # Determine the colors of each segment
                s_colors = [colors[0]]
                s_colors.extend(colors[s_idx])
                s_colors = np.array(s_colors)

                # Set the values of the line-collection to be these colors
                lc.set_array(s_colors)

                # Add line-collection to this subplot
                ax1.add_collection(lc)

            # Add gray-scale colormap subplot
            ax1.imshow(rgb_L[np.newaxis, ...], aspect='auto')

            # Plot the name of the colormap as text
            x_text = pos0.x0-0.01
            y_text = pos0.y0+pos0.height/2
            fig.text(x_text, y_text, cmap.name,
                     va='center', ha='right', fontsize=10)

    # If savefig is not None, save the figure
    if savefig is not None:
        dpi = 100 if (path.splitext(savefig)[1] == '.svg') else 250
        plt.savefig(savefig, dpi=dpi)
        plt.close(fig)

    # Else, simply show it
    else:
        plt.show()


# Define function that prints a string with the BibTeX entry to CMasher's paper
def get_bibtex():
    """
    Prints a string that gives the BibTeX entry for citing the *CMasher* paper
    (Van der Velden 2020, JOSS, 5, 2004).

    """

    # Create string with BibTeX entry
    bibtex = dedent(
        r"""
        @ARTICLE{2020JOSS....5.2004V,
            author = {{van der Velden}, Ellert},
            title = "{CMasher: Scientific colormaps for making accessible,
                informative and 'cmashing' plots}",
            journal = {The Journal of Open Source Software},
            keywords = {Python, science, colormaps, data visualization,
                plotting, Electrical Engineering and Systems Science - Image
                and Video Processing, Physics - Data Analysis, Statistics and
                Probability},
            year = 2020,
            month = feb,
            volume = {5},
            number = {46},
            eid = {2004},
            pages = {2004},
            doi = {10.21105/joss.02004},
            archivePrefix = {arXiv},
            eprint = {2003.01069},
            primaryClass = {eess.IV},
            adsurl = {https://ui.adsabs.harvard.edu/abs/2020JOSS....5.2004V},
            adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
        """)

    # Print the string
    print(bibtex.strip())


# This function determines the colormap type of a given colormap
def get_cmap_type(cmap):
    """
    Checks what the colormap type (sequential; diverging; cyclic; qualitative;
    misc) of the provided `cmap` is and returns it.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    cm_type : {'sequential'; 'diverging'; 'cyclic'; 'qualitative'; 'misc'}
        A string stating which of the defined colormap types the provided
        `cmap` has.

    """

    # Obtain the colormap
    cmap = mplcm.get_cmap(cmap)

    # Get RGB values for colormap
    rgb = cmap(np.arange(cmap.N))[:, :3]

    # Get lightness values of colormap
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    L = lab[:, 0]
    diff_L = np.diff(L)

    # Obtain central values of lightness
    N = cmap.N-1
    central_i = [int(np.floor(N/2)), int(np.ceil(N/2))]
    diff_L0 = np.diff(L[:central_i[0]+1])
    diff_L1 = np.diff(L[central_i[1]:])

    # Obtain perceptual differences of last two and first two values
    lab_red = lab[[-2, -1, 0, 1]]
    deltas = np.sqrt(np.sum(np.diff(lab_red, axis=0)**2, axis=-1))

    # Check the statistics of cmap and determine the colormap type
    # QUALITATIVE
    # If the colormap has less than 40 values, assume it is qualitative
    if(cmap.N < 40):
        return('qualitative')

    # MISC 1
    # If the colormap has only a single lightness, it is misc
    elif np.allclose(diff_L, 0):
        return('misc')

    # SEQUENTIAL
    # If the lightness values always increase or decrease, it is sequential
    elif np.isclose(np.abs(np.sum(diff_L)), np.sum(np.abs(diff_L))):
        return('sequential')

    # DIVERGING
    # If the lightness values have a central extreme and sequential sides
    # Then it is diverging
    elif (np.isclose(np.abs(np.sum(diff_L0)), np.sum(np.abs(diff_L0))) and
          np.isclose(np.abs(np.sum(diff_L1)), np.sum(np.abs(diff_L1)))):
        # If the perceptual difference between the last and first value is
        # comparable to the other perceptual differences, it is cyclic
        if(np.all(np.abs(np.diff(deltas)) < deltas[::2]) and
           np.diff(deltas[::2])):
            return('cyclic')

        # Otherwise, it is a normal diverging colormap
        else:
            return('diverging')

    # MISC 2
    # If none of the criteria above apply, it is misc
    else:
        return('misc')


# Function create a colormap using a subset of the colors in an existing one
def get_sub_cmap(cmap, start, stop):
    """
    Creates a :obj:`~matplotlib.cm.ListedColormap` object using the colors in
    the range `[start, stop]` of the provided `cmap` and returns it.

    This function can be used to create a colormap that only uses a portion of
    an existing colormap.

    .. versionadded:: 1.3.2

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.
    start, stop : float
        The normalized range of the colors in `cmap` that must be in the sub
        colormap.

    Returns
    -------
    sub_cmap : :obj:`~matplotlib.colors.ListedColormap`
        The created colormap that uses a subset of the colors in `cmap`.

    Example
    -------
    Creating a colormap using the first 80% of the 'rainforest' colormap::

        >>> get_sub_cmap('cmr.rainforest', 0, 0.8)

    Notes
    -----
    As it can create artifacts, this function does not interpolate between the
    colors in `cmap` to fill up the space. Therefore, using values for `start`
    and `stop` that are too close to each other, may result in a colormap that
    contains too few different colors to be smooth.
    It is recommended to use at least 128 different colors in a colormap for
    optimal results (*CMasher* colormaps have 256 or 511 different colors, for
    sequential or diverging colormaps respectively).
    One can check the number of colors in a colormap with
    :attr:`matplotlib.colors.Colormap.N`.

    Any colormaps created using this function are not registered in either
    *CMasher* or *MPL*.

    """

    # Obtain the colormap
    cmap = mplcm.get_cmap(cmap)

    # Obtain colors
    colors = take_cmap_colors(cmap, None, cmap_range=(start, stop))

    # Create new colormap
    sub_cmap = LC(colors, cmap.name+'_sub', N=len(colors))

    # Return sub_cmap
    return(sub_cmap)


# Function to import all custom colormaps in a file or directory
def import_cmaps(cmap_path):
    """
    Reads in custom colormaps from a provided file or directory `cmap_path`;
    transforms them into :obj:`~matplotlib.colors.ListedColormap` objects; and
    makes them available in the :mod:`cmasher.cm` module, in addition to
    registering them in the :mod:`matplotlib.cm` module.
    Both the imported colormap and its reversed version will be registered.

    If a provided colormap is a 'cyclic' colormap, its shifted version will
    also be registered.

    Parameters
    ----------
    cmap_path : str
        Relative or absolute path to a custom colormap file; or directory that
        contains custom colormap files. A colormap file can be a *NumPy* binary
        file ('.npy'); a *viscm* source file ('.jscm'); or any text file.
        If the file is not a JSCM-file, it must contain the normalized; 8-bit;
        or hexadecimal string RGB values that define the colormap.

    Notes
    -----
    All colormap files must have names starting with the 'cm\\_' prefix. The
    resulting colormaps will have the name of their file without the prefix and
    extension.

    In *MPL*, the colormaps will have the added 'cmr.' prefix to avoid name
    clashes.

    Example
    -------
    Importing a colormap named 'test' can be done by saving its normalized RGB
    values in a file called 'cm_test.txt' and executing

        >>> import_cmaps('/path/to/dir/cm_test.txt')

    The 'test' colormap is now available in *CMasher* and *MPL* using

        >>> cmr.cm.test                 # CMasher
        >>> plt.get_cmap('cmr.test')    # MPL

    """

    # Obtain path to file or directory with colormaps
    cmap_path = path.abspath(cmap_path)

    # Check if provided file or directory exists
    if not path.exists(cmap_path):
        raise OSError("Input argument 'cmap_path' is a non-existing path (%r)!"
                      % (cmap_path))

    # Check if cmap_path is a file or directory and act accordingly
    if path.isfile(cmap_path):
        # If file, split cmap_path up into dir and file components
        cmap_dir, cmap_file = path.split(cmap_path)

        # Check if its name starts with 'cm_' and raise error if not
        if not cmap_file.startswith('cm_'):
            raise OSError("Input argument 'cmap_path' does not lead to a file "
                          "with the 'cm_' prefix (%r)!" % (cmap_path))

        # Set cm_files to be the sole read-in file
        cm_files = [cmap_file]
    else:
        # If directory, obtain the names of all colormap files in cmap_path
        cmap_dir = cmap_path
        cm_files = list(map(path.basename, glob("%s/cm_*" % (cmap_dir))))
        cm_files.sort()

    # Read in all the defined colormaps, transform and register them
    for cm_file in cm_files:
        # Split basename and extension
        base_str, ext_str = path.splitext(cm_file)
        cm_name = base_str[3:]

        # Obtain absolute path to colormap data file
        cm_file_path = path.join(cmap_dir, cm_file)

        # Process colormap files
        try:
            # If file is a NumPy binary file
            if(ext_str == '.npy'):
                rgb = np.load(cm_file_path)

            # If file is viscm source file
            elif(ext_str == '.jscm'):
                # Check if viscm is available
                try:
                    import viscm
                # If that fails, raise error
                except ImportError:  # pragma: no cover
                    raise ImportError("The 'viscm' package is required to read"
                                      " '.jscm' files!")
                # If that succeeds, load RGB values from source file
                else:
                    # Load colormap
                    cmap = viscm.gui.Colormap(None, None, None)
                    cmap.load(cm_file_path)

                    # Create editor and obtain RGB values
                    v = viscm.viscm_editor(uniform_space=cmap.uniform_space,
                                           cmtype=cmap.cmtype,
                                           method=cmap.method,
                                           **cmap.params)
                    rgb, _ = v.cmap_model.get_sRGB()

            # If file is anything else
            else:
                rgb = np.genfromtxt(cm_file_path, dtype=None, comments='//',
                                    encoding=None)

            # Register colormap
            register_cmap(cm_name, rgb)

            # Check if provided cmap is a cyclic colormap
            # If so, obtain its shifted (reversed) versions as well
            if(get_cmap_type('cmr.'+cm_name) == 'cyclic'):
                # Determine the central value index of the colormap
                idx = len(rgb)//2

                # Shift the entire colormap by this index
                rgb_s = np.concatenate([rgb[idx:], rgb[:idx]], axis=0)

                # Register this colormap as well
                register_cmap(cm_name+'_shifted', rgb_s)

        # If any error is raised, reraise it
        except Exception as error:
            raise ValueError("Provided colormap %r is invalid! (%s)"
                             % (cm_name, error))


# Function to register a custom colormap in MPL and CMasher
def register_cmap(name, data):
    """
    Creates a :obj:`~matplotlib.colors.ListedColormap` object using the
    provided `name` and `data`, and registers the colormap in the
    :mod:`cmasher.cm` and :mod:`matplotlib.cm` modules.
    A reversed version of the colormap will be registered as well.

    Parameters
    ----------
    name : str
        The name that this colormap must have.
    data : 2D array_like of {float; int} with shape `(N, 3)` or 1D array_like \
        of str with shape `(N, )`
        An array containing the RGB values of all segments in the colormap.
        If float, the array contains normalized RGB values.
        If int, the array contains 8-bit RGB values.
        If str, the array contains hexadecimal string RGB values.

    Note
    ----
    In *MPL*, the colormap will have the added 'cmr.' prefix to avoid name
    clashes.

    """

    # Convert provided data to a NumPy array
    cm_data = np.array(data)

    # Check the type of the data
    if issubclass(cm_data.dtype.type, str):
        # If the values are strings, make sure they start with a '#'
        cm_data = map(lambda x: '#'+x if not x.startswith('#') else x, cm_data)

        # Convert all values to floats
        colorlist = list(map(to_rgb, cm_data))

    else:
        # Make sure that cm_data is 2D
        cm_data = np.array(cm_data, copy=False, ndmin=2)

        # If the values are integers, divide them by 255
        if issubclass(cm_data.dtype.type, np.integer):
            cm_data = cm_data/255

        # Convert cm_data to a list
        colorlist = cm_data.tolist()

    # Transform colorlist into a Colormap
    cmap_N = len(colorlist)
    cmap_mpl = LC(colorlist, 'cmr.'+name, N=cmap_N)
    cmap_cmr = LC(colorlist, name, N=cmap_N)
    cmap_mpl_r = cmap_mpl.reversed()
    cmap_cmr_r = cmap_cmr.reversed()

    # Test that the colormaps can be called
    cmap_mpl(1)
    cmap_mpl_r(1)

    # Determine the cm_type of the colormap
    cm_type = get_cmap_type(cmap_mpl)

    # Add cmap to matplotlib's cmap list
    mplcm.register_cmap(cmap=cmap_mpl)
    setattr(cmrcm, cmap_cmr.name, cmap_cmr)
    cmrcm.__all__.append(cmap_cmr.name)
    cmrcm.cmap_d[cmap_cmr.name] = cmap_cmr
    cmrcm.cmap_cd[cm_type][cmap_cmr.name] = cmap_cmr

    # Add reversed cmap to matplotlib's cmap list
    mplcm.register_cmap(cmap=cmap_mpl_r)
    setattr(cmrcm, cmap_cmr_r.name, cmap_cmr_r)
    cmrcm.__all__.append(cmap_cmr_r.name)
    cmrcm.cmap_d[cmap_cmr_r.name] = cmap_cmr_r
    cmrcm.cmap_cd[cm_type][cmap_cmr_r.name] = cmap_cmr_r


# Function to set the legend label of an artist that uses a colormap
def set_cmap_legend_entry(artist, label):
    """
    Sets the label of the provided `artist` to `label`, and creates a legend
    entry using a miniature version of the colormap of `artist` as the legend
    icon.

    This function can be used to add legend entries for *MPL* artists that use
    a colormap, like those made with :func:`~matplotlib.pyplot.hexbin`;
    :func:`~matplotlib.pyplot.hist2d`; :func:`~matplotlib.pyplot.scatter`; or
    any :mod:`~matplotlib.pyplot` function that takes `cmap` as an input
    argument.
    Keep in mind that using this function will override any legend entry that
    already exists for `artist`.

    Parameters
    ----------
    artist : :obj:`~matplotlib.artist.Artist` object
        Any artist object that has the `cmap` attribute, for which a legend
        entry must be made using its colormap as the icon.
    label : str
        The string that must be set as the label of `artist`.

    """

    # Obtain the colormap of the provided artist
    cmap = getattr(artist, 'cmap', None)

    # If cmap is None, raise error
    if cmap is None:
        raise ValueError("Input argument 'artist' does not have attribute "
                         "'cmap'!")

    # Set the label of this artist
    artist.set_label(label)

    # Add the HandlerColorPolyCollection to the default handler map for artist
    Legend.get_default_handler_map()[artist] = _HandlerColorPolyCollection()


# Function to take N equally spaced colors from a colormap
def take_cmap_colors(cmap, N, *, cmap_range=(0, 1), return_fmt='float'):
    """
    Takes `N` equally spaced colors from the provided colormap `cmap` and
    returns them.

    .. versionadded:: 1.3.2

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.
    N : int or None
        The number of colors to take from the provided `cmap`.
        If *None*, take all colors in `cmap` within the provided `cmap_range`.

    Optional
    --------
    cmap_range : tuple of float. Default: (0, 1)
        The normalized value range in the colormap from which colors should be
        taken.
        By default, colors are taken from the entire colormap.
    return_fmt : {'float'/'norm'; 'int'/'8bit'; 'str'/'hex'}. Default: 'float'
        The format of the requested colors.
        If 'float'/'norm', the colors are returned as normalized RGB tuples.
        If 'int'/'8bit', the colors are returned as 8-bit RGB tuples.
        If 'str'/'hex', the colors are returned using their hexadecimal string
        representations.

    Returns
    -------
    colors : list of {tuple; str}
        The colors that were taken from the provided `cmap`.

    Examples
    --------
    Taking five equally spaced colors from the 'rainforest' colormap::

        >>> take_cmap_colors('cmr.rainforest', 5)
        [(0.0, 0.0, 0.0),
         (0.226123592, 0.124584033, 0.562997277),
         (0.0548210513, 0.515835251, 0.45667819),
         (0.709615979, 0.722863985, 0.0834727592),
         (1.0, 1.0, 1.0)]

    Requesting their 8-bit RGB values instead::

        >>> take_cmap_colors('cmr.rainforest', 5, return_fmt='int')
        [(0, 0, 0),
         (58, 32, 144),
         (14, 132, 116),
         (181, 184, 21),
         (255, 255, 255)]

    Requesting HEX-code values instead::

        >>> take_cmap_colors('cmr.rainforest', 5, return_fmt='hex')
        ['#000000', '#3A2090', '#0E8474', '#B5B815', '#FFFFFF']

    Requesting colors in a specific range::

        >>> take_cmap_colors('cmr.rainforest', 5, cmap_range=(0.2, 0.8),
                             return_fmt='hex')
        ['#3E0374', '#10528A', '#0E8474', '#5CAD3C', '#D6BF4A']

    Note
    ----
    Using this function on a perceptually uniform sequential colormap, like
    those in *CMasher*, allows one to pick a number of line colors that are
    different but still sequential. This is useful when plotting a set of lines
    that describe the same property, but have a different initial state.

    """

    # Convert provided fmt to lowercase
    return_fmt = return_fmt.lower()

    # Obtain the colormap
    cmap = mplcm.get_cmap(cmap)

    # Check if provided cmap_range is valid
    if not ((0 <= cmap_range[0] <= 1) and (0 <= cmap_range[1] <= 1)):
        raise ValueError("Input argument 'cmap_range' does not contain "
                         "normalized values!")

    # Extract and convert start and stop to their integer indices (inclusive)
    start = int(np.floor(cmap_range[0]*cmap.N))
    stop = int(np.ceil(cmap_range[1]*cmap.N))-1

    # Pick colors
    if N is None:
        index = np.arange(start, stop+1, dtype=int)
    else:
        index = np.array(np.rint(np.linspace(start, stop, num=N)), dtype=int)
    colors = cmap(index)

    # Convert colors to proper format
    if return_fmt in ('float', 'norm', 'int', '8bit'):
        colors = np.apply_along_axis(to_rgb, 1, colors)
        if return_fmt in ('int', '8bit'):
            colors = np.array(np.rint(colors*255), dtype=int)
        colors = list(map(tuple, colors))
    else:
        colors = list(map((lambda x: to_hex(x).upper()), colors))

    # Return colors
    return(colors)


# %% IMPORT SCRIPT
# Import all colormaps defined in './colormaps'
import_cmaps(path.join(path.dirname(__file__), 'colormaps'))
