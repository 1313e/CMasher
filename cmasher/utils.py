# -*- coding: utf-8 -*-

"""
Utils
=====
Utility functions required for registering all defined scientific colormaps.

"""


# %% IMPORTS
# Future imports
from __future__ import absolute_import, division, print_function

# Built-in imports
from collections import OrderedDict as odict
import os
from os import path
from textwrap import dedent

# Package imports
from colorspacious import cspace_converter
from matplotlib import cm as mplcm
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap as LC
import matplotlib.pyplot as plt
import numpy as np
from six import string_types

# CMasher imports
from cmasher import cm as cmrcm

# All declaration
__all__ = ['create_cmap_overview', 'get_bibtex', 'import_cmaps']


# %% HELPER FUNCTIONS
# This function determines the colormap type of a given colormap
def _get_cm_type(cmap):
    """
    Checks what the colormap type (sequential; diverging; cyclic; qualitative;
    misc) of the provided `cmap` is and returns it.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in *MPL* or its corresponding
        :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    cm_type : {'sequential'; 'diverging'; 'cyclic'; 'qualitative'; 'misc'}
        A string stating which of the defined colormap types the provided
        `cmap` has.

    """

    # Obtain the colormap
    cmap = mplcm.get_cmap(cmap)

    # Get array of all values for which a colormap value is requested
    x = np.linspace(0, 1, cmap.N)

    # Get RGB values for colormap
    rgb = cmap(x)[:, :3]

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
    # If the colormap has plateaus in lightness, it is misc
    elif np.any(np.isclose(diff_L0, 0)) or np.any(np.isclose(diff_L1, 0)):
        return('misc')

    # SEQUENTIAL
    # If the lightness values always increase or decrease, it is sequential
    elif (np.isclose(np.abs(np.sum(diff_L)), np.sum(np.abs(diff_L))) and
          not np.any(np.isclose(diff_L, 0))):
        return('sequential')

    # DIVERGING
    # If the lightness values have a central extreme and sequential sides
    # Then it is diverging
    elif (np.isclose(np.abs(np.sum(diff_L0)), np.sum(np.abs(diff_L0))) and
          np.isclose(np.abs(np.sum(diff_L1)), np.sum(np.abs(diff_L1)))):
        # If the perceptual difference between the last and first value is
        # comparable to the other perceptual differences, it is cyclic
        if np.all(np.abs(np.diff(deltas)) < deltas[::2]):
            return('cyclic')

        # Otherwise, it is a normal diverging colormap
        else:
            return('diverging')

    # MISC 2
    # If none of the criteria above apply, it is misc
    else:
        return('misc')


# Define function for obtaining the sorting order for lightness ranking
def _get_cmap_lightness_rank(cmap):
    """
    Returns a tuple of objects used for sorting the provided `cmap` based
    on its lightness profile.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in *MPL* or its corresponding
        :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    L_start : float
        The starting lightness value of `cmap`.
    L_rmse : float
        The RMSE of the lightness profile of `cmap`.
        For diverging colormaps, this is the max RMSE of either half.
    L_rng : float
        The lightness range (L_max-L_min) of `cmap`.
    name : str
        The name of `cmap`.

    """

    # Obtain the colormap
    cmap = mplcm.get_cmap(cmap)

    # Get array of all values for which a colormap value is requested
    x = np.linspace(0, 1, cmap.N)

    # Get RGB values for colormap
    rgb = cmap(x)[:, :3]

    # Get lightness values of colormap
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    L = lab[:, 0]

    # Determine the deltas of the lightness profile
    deltas = np.diff(L)
    derivs = (cmap.N-1)*deltas

    # Determine the RMSE of the lightness profile
    if _get_cm_type(cmap) in ('diverging', 'cyclic'):
        # If cmap is diverging, calculate RMSE of both halves
        central_i = [int(np.floor(cmap.N/2)), int(np.ceil(cmap.N/2))]
        L_rmse = np.max([np.around(np.std(derivs[:central_i[0]]), 1),
                         np.around(np.std(derivs[central_i[1]:]), 1)])
    else:
        # Else, take RMSE of entire lightness profile
        L_rmse = np.around(np.std(derivs), 1)

    # Determine start and range
    L_start = np.around(L[0], 1)
    L_min = np.around(np.min(L), 1)
    L_max = np.around(np.max(L), 1)
    L_rng = np.around(np.abs(L_max-L_min), 1)

    # Return contributions to the rank
    return(L_start, L_rmse, L_rng, cmap.name)


# %% FUNCTIONS
# This function creates an overview plot of all colormaps specified
def create_cmap_overview(cmaps=None, savefig=None, use_types=True,
                         sort='alphabetical', plot_profile=False):
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
    sort : {'alphabetical'/'name'; 'lightness'}. Default: 'alphabetical'
        String indicating how the colormaps should be sorted in the overview.
        If 'alphabetical', the colormaps are sorted alphabetically on their
        name.
        If 'lightness', the colormaps are sorted on their starting lightness
        and their lightness range.
    plot_profile : bool or int. Default: False
        Whether the lightness profiles of all colormaps should be plotted. If
        not *False*, the lightness profile of a colormap is plotted on top of
        its gray-scale version and `plot_profile` is used for setting the alpha
        (opacity) value.
        If `plot_profile` is *True*, it will be set to `0.25`.

    Notes
    -----
    The colormaps in `cmaps` can either be provided as their registered name in
    *MPL*, or their corresponding :obj:`~matplotlib.colors.Colormap` object.
    Any provided reversed colormaps (colormaps that end their name with '_r')
    are ignored.

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
                if isinstance(cmap, string_types):
                    if not cmap.endswith('_r'):
                        cmaps_dict[cm_type].append(mplcm.get_cmap(cmap))
                elif not cmap.name.endswith('_r'):
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
                cm_type = _get_cm_type(cmap)
                if isinstance(cmap, string_types):
                    if not cmap.endswith('_r'):
                        cmaps_dict[cm_type].append(mplcm.get_cmap(cmap))
                elif not cmap.name.endswith('_r'):
                    cmaps_dict[cm_type].append(cmap)
        else:
            # Loop over all cmaps and remove reversed versions
            for cmap in cmaps:
                if isinstance(cmap, string_types):
                    if not cmap.endswith('_r'):
                        cmaps_list.append(mplcm.get_cmap(cmap))
                elif not cmap.name.endswith('_r'):
                    cmaps_list.append(cmap)

    # If use_types is True, a dict is currently used
    if use_types:
        # Convert entire cmaps_dict into a list again
        for key, value in cmaps_dict.items():
            # If this cm_type has at least 1 colormap, sort and add them
            if value:
                # Sort this cm_type on name
                value.sort(key=lambda x: x.name)

                # Sort on lightness if requested and this cm_type is compatible
                if((sort.lower() == 'lightness') and
                   (key not in ('qualitative', 'misc'))):
                    value.sort(key=_get_cmap_lightness_rank)

                # Add to list
                cmaps_list.append(key)
                cmaps_list.extend(value)

    # Else, a list is used
    else:
        # Sort the colormaps
        cmaps_list.sort(key=lambda x: x.name)
        if(sort.lower() == 'lightness'):
            cmaps_list.sort(key=_get_cmap_lightness_rank)

    # Obtain the colorspace converter for showing cmaps in grey-scale
    cspace_convert = cspace_converter("sRGB1", "CAM02-UCS")

    # Create figure instance
    height = 0.4*(len(cmaps_list)+1)
    fig, axes = plt.subplots(figsize=(6.4, height),
                             nrows=len(cmaps_list), ncols=2)
    fig.subplots_adjust(top=(1-0.24/height), bottom=0.048/height, left=0.2,
                        right=0.99, wspace=0.05)
    fig.suptitle("Colormap Overview", fontsize=16, y=1.0, x=0.595)

    # If cmaps_list only has a single element, make sure axes is a list
    if(len(cmaps_list) == 1):
        axes = [axes]

    # Set the current cm_type to None
    cm_type = None

    # Loop over all cmaps defined in cmaps list
    for ax, cmap in zip(axes, cmaps_list):
        # Turn axes off
        ax[0].set_axis_off()
        ax[1].set_axis_off()

        # If cmap is a string, it defines a cm_type
        if isinstance(cmap, string_types):
            # Write the cm_type as text in the correct position
            fig.text(0.595, ax[0].get_position().bounds[1], cmap,
                     va='bottom', ha='center', fontsize=14)

            # Save what the current cm_type is
            cm_type = cmap

        # Else, this is a colormap
        else:
            # Get array of all values for which a colormap value is requested
            x = np.linspace(0, 1, cmap.N)

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
            ax[0].imshow(rgb[np.newaxis, ...], aspect='auto')

            # Check if the lightness profile was requested
            if plot_profile and (cm_type != 'qualitative'):
                # Determine the points that need to be plotted
                plot_x = np.arange(cmap.N)
                plot_L = -(L-0.5)
                points = np.stack([plot_x, plot_L], axis=1)

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
                ax[1].add_collection(lc)

            # Add gray-scale colormap subplot
            ax[1].imshow(rgb_L[np.newaxis, ...], aspect='auto')

            # Plot the name of the colormap as text
            pos = list(ax[0].get_position().bounds)
            x_text = pos[0]-0.01
            y_text = pos[1]+pos[3]/2
            fig.text(x_text, y_text, cmap.name, va='center', ha='right',
                     fontsize=10)

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


# Function to import all custom colormaps in a file or directory
def import_cmaps(cmap_path):
    """
    Reads in custom colormaps from a provided file or directory `cmap_path`;
    transforms them into :obj:`~matplotlib.colors.ListedColormap` objects; and
    makes them available in the :mod:`cmasher.cm` module, in addition to
    registering them in the :mod:`matplotlib.cm` module.
    Both the imported colormap and its reversed version will be registered.

    Parameters
    ----------
    cmap_path : str
        Relative or absolute path to a custom colormap file; or directory that
        contains custom colormap files. A colormap file can be a *NumPy* binary
        file ('.npy'); a *viscm* source file ('.jscm'); or any text file.
        If the file is not a JSCM-file, it must contain the normalized RGB
        values that define the colormap.

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
        # If directory, obtain the names of all files in cmap_path
        cmap_dir = cmap_path
        filenames = next(os.walk(cmap_dir))[2]

        # Extract the files with defined colormaps
        cm_files = [name for name in filenames if name.startswith('cm_')]
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
                colorlist = np.load(cm_file_path).tolist()

            # If file is viscm source file
            elif(ext_str == '.jscm'):
                # Check if viscm is available
                try:
                    import viscm
                # If that fails, raise error
                except ImportError:
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
                    rgb, _ = v.cmap_model.get_sRGB(num=256)
                    colorlist = rgb.tolist()

            # If file is anything else
            else:
                colorlist = np.genfromtxt(cm_file_path).tolist()

            # Transform colorlist into a Colormap
            cmap_mpl = LC(colorlist, 'cmr.'+cm_name, N=len(colorlist))
            cmap_cmr = LC(colorlist, cm_name, N=len(colorlist))
            cmap_mpl_r = cmap_mpl.reversed()
            cmap_cmr_r = cmap_cmr.reversed()

            # Test that the colormaps can be called
            cmap_mpl(1)
            cmap_mpl_r(1)

            # Determine the cm_type of the colormap
            cm_type = _get_cm_type(cmap_mpl)

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

        # If any error is raised, reraise it
        except Exception as error:
            raise ValueError("Provided colormap %r is invalid! (%s)"
                             % (cm_name, error))


# Import all colormaps defined in './colormaps'
import_cmaps(path.join(path.dirname(__file__), 'colormaps'))
