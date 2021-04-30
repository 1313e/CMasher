# -*- coding: utf-8 -*-

"""
Application usage
=================
Holds function definitions useful for porting *CMasher* colormaps to other
applications.

"""


# %% IMPORTS
# Built-in imports
from os import path
import re
from textwrap import dedent, indent

# Import packages
import cmasher as cmr

# All declaration
__all__ = ['update_tableau_pref_file']


# %% FUNCTION DEFINITIONS
# Define function that generates a Tableau properties file with colormaps
def update_tableau_pref_file(dirname='.'):
    """
    Update an existing Tableau 'Preferences.tps' file to include colormaps from
    *CMasher*.

    The file is created if it does not exist yet.

    Optional
    --------
    dirname : str. Default: '.'
        The relative or absolute path to the directory where the Tableau
        preferences file should be updated.
        If `dirname` contains an existing file called 'Preferences.tps', it
        will be updated to include *CMasher* colormap data.
        Otherwise, this file will be created in `dirname`.

    Note
    ----
    In *CMasher*, colormaps sometimes get modified or renamed. This function
    takes these cases into account as well.

    """

    # Obtain all colormaps in CMasher without reversed versions
    # This is because Tableau already has a function for this
    cmaps = [y for y in cmr.cm.cmap_d.values() if not y.name.endswith('_r')]

    # Create a dict that contains the Tableau type for each colormap type
    cmap_types = {
        'sequential': 'ordered-sequential',
        'diverging': 'ordered-diverging',
        'cyclic': 'regular'}

    # Create empty dict of color-palette entries for all colormaps
    entries_dict = {}

    # Loop over all colormaps and create their color-palette entries
    for cmap in cmaps:
        # Obtain the type of this colormap
        cmap_type = cmap_types[cmr.get_cmap_type(cmap)]

        # Obtain all colors of this colormap in HEX-format
        colors_hex = cmr.take_cmap_colors(cmap, N=None, return_fmt='hex')

        # Create a list with all color representations in HEX
        colors_list = list(map(lambda x: "<color>%s</color>" % (x),
                               colors_hex))

        # Combine all these colors into a single string
        colors_str = '\n'.join(colors_list)

        # Make sure to indent all lines in this string by 1 tab
        colors_str = indent(colors_str, '\t').expandtabs(4)

        # Create color-palette entry string
        entry_str = dedent("""
            <color-palette name="cmr.{0}" type="{1}">
            {2}
            </color-palette>""").format(
            cmap.name, cmap_type, colors_str)[1:]

        # Indent this string by 1 tab
        entry_str = indent(entry_str, '\t').expandtabs(4)

        # Add this entry to the dict
        entries_dict[cmap.name] = entry_str

    # Obtain absolute path to preferences file in provided dirname
    filename = path.abspath(path.join(dirname, 'Preferences.tps'))

    # Check if this file already exists
    if path.exists(filename):
        # If so, read in the file contents
        with open(filename, 'r') as f:
            text = f.read()

        # Define the strings that enclose the colormap entries usually
        start_str = "<workbook>\n    <preferences>\n"
        end_str = "\n    </preferences>\n</workbook>"

        # Search for these strings
        start_idx = text.find(start_str)+29
        end_idx = text.find(end_str)
        sub_contents = text[start_idx:end_idx]

        # Now search this sub_contents string for all colormap names
        cmap_names = re.findall(r"\"cmr\.(\w+)\"", sub_contents)

        # Search entries_dict for all cmap_names
        for cmap in cmap_names:
            # Check if cmap is in entries_dict
            if cmap not in entries_dict:
                # If not, obtain the entire entry
                idx = sub_contents.find('cmr.'+cmap)
                start_idx_entry = idx-25
                match = re.search(r"<\/color-palette>\n",
                                  sub_contents[start_idx_entry:])
                end_idx_entry = match.end()+start_idx_entry

                # Remove this entry from sub_contents
                sub_contents = ''.join([sub_contents[:start_idx_entry],
                                        sub_contents[end_idx_entry:]])

        # Search this sub_contents string for all strings in entries_dict
        for cmap, cmap_entry in dict(entries_dict).items():
            # Check if this colormap name already exists
            idx = sub_contents.find('cmr.'+cmap)
            if(idx != -1):
                # If so, obtain the entire entry
                start_idx_entry = idx-25
                match = re.search(r"<\/color-palette>",
                                  sub_contents[start_idx_entry:])
                end_idx_entry = match.end()+start_idx_entry

                # Replace this entry with the new entry
                sub_contents = ''.join([sub_contents[:start_idx_entry],
                                        cmap_entry,
                                        sub_contents[end_idx_entry:]])

                # Remove cmap from entries_dict
                entries_dict.pop(cmap)

        # Combine everything remaining in entries_dict together
        entries_str = '\n'.join(['', *entries_dict.values()])

        # Join sub_contents and entries_str together
        sub_contents = ''.join([sub_contents, entries_str])

        # Insert the sub_contents into pref_file_contents
        text = ''.join([text[:start_idx], sub_contents, text[end_idx:]])

        # Save this to the preferences file
        with open(filename, 'w') as f:
            f.write(text)

    else:
        # If not, combine everything in entries_dict together to single string
        entries_str = '\n'.join(entries_dict.values())

        # Create the string for the new 'Preferences.tps' file
        pref_file = dedent("""
            <?xml version='1.0'?>
            <workbook>
                <preferences>
            {0}
                </preferences>
            </workbook>""").format(entries_str)[1:]

        # Create this file
        with open(filename, 'w') as f:
            f.write(pref_file)
