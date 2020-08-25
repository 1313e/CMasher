# -*- coding: utf-8 -*-

# %% IMPORTS
# Built-in imports
import argparse
from importlib import import_module
import os
import sys

# Package imports
import e13tools as e13
from matplotlib import cm as mplcm
import numpy as np

# CMasher imports
from cmasher import __version__
import cmasher as cmr

# All declaration
__all__ = ['main']


# %% GLOBALS
# Define main description of this package
main_desc = ("CMasher: Scientific colormaps for making accessible, informative"
             " and 'cmashing' plots")


# %% CLASS DEFINITIONS
# Define formatter that automatically extracts help strings of subcommands
class HelpFormatterWithSubCommands(argparse.ArgumentDefaultsHelpFormatter):
    # Override the add_argument function
    def add_argument(self, action):
        # Check if the help of this action is required
        if action.help is not argparse.SUPPRESS:
            # Check if this action is a subparser's action
            if isinstance(action, argparse._SubParsersAction):
                # If so, sort action.choices on name
                names = sorted(action.choices.keys())

                # Loop over all subcommands defined in the action
                for name in names:
                    # Obtain corresponding subparser
                    subparser = action.choices[name]

                    # Format the description of this subcommand and add it
                    self._add_item(self.format_subcommands,
                                   [name, subparser.description])
            # Call super method in all other cases
            else:
                super().add_argument(action)

    # This function formats the description of a subcommand with given name
    def format_subcommands(self, name, description):
        # Determine the positions and widths of the help texts
        help_position = min(self._action_max_length+2, self._max_help_position)
        help_width = max(self._width-help_position, 11)
        name_width = help_position-self._current_indent-2

        # Transform name to the proper formatting
        name = "{0}{1: <{2}}{3}".format(
            ' '*self._current_indent, name, name_width,
            '  ' if(len(name) <= name_width) else '\n'+' '*help_position)

        # Split the lines of the subcommand description
        desc_lines = self._split_lines(description, help_width)

        # Create list of all parts of the description of this subcommand
        parts = [name, desc_lines.pop(0), '\n']

        # Loop over all remaining desc_lines
        for line in desc_lines:
            # Format and add to parts
            parts.append("%s%s\n" % (' '*help_position, line))

        # Convert to a single string and return
        return(''.join(parts))


# %% COMMAND FUNCTION DEFINITIONS
# This function handles the 'bibtex' subcommand
def cli_bibtex():
    cmr.get_bibtex()


# This function handles the 'cmap_type' subcommand
def cli_cmap_type():
    # Import cmap packages
    import_cmap_pkgs()

    # Print cmap type
    print(cmr.get_cmap_type(get_cmap(ARGS.cmap)))


# This function handles the 'take_cmap_colors' subcommand
def cli_cmap_colors():
    # Import cmap packages
    import_cmap_pkgs()

    # Obtain the colors
    colors = cmr.take_cmap_colors(get_cmap(ARGS.cmap), ARGS.ncolors,
                                  cmap_range=ARGS.cmap_range,
                                  return_fmt=ARGS.return_fmt)

    # Print the colors line-by-line
    if ARGS.return_fmt in ('float', 'norm'):
        np.savetxt(sys.stdout, colors, '%.8f')
    elif ARGS.return_fmt in ('int', '8bit'):
        np.savetxt(sys.stdout, colors, '%i')
    else:
        np.savetxt(sys.stdout, colors, '%s')


# This function handles the 'mkcmod' subcommand
def cli_mk_cmod():
    # Create cmap module
    cmap_path = cmr.create_cmap_mod(ARGS.cmap, save_dir=ARGS.dir)

    # Print on commandline that module has been created
    print("Created standalone colormap module of %r in %r."
          % (ARGS.cmap, cmap_path))


# %% FUNCTION DEFINITIONS
# This function obtains the colormap that was requested
def get_cmap(cmap):
    # Try to obtain the colormap from MPL
    try:
        cmap = mplcm.get_cmap(cmap)

    # If this does not work, try to expand given cmap in setuptools-style
    except ValueError:
        # Check if cmap contains a colon
        if ':' in cmap:
            # Split cmap up into mod_name and obj_name
            mod_name, obj_name = cmap.split(':', 1)
            obj_path = obj_name.split('.')

            # Import the provided module as cmap
            cmap = import_module(mod_name)

            # Import the provided object from this module
            for obj in obj_path:
                cmap = getattr(cmap, obj)

    # If cmap is still a string, raise error
    if isinstance(cmap, str):
        # Print error and exit
        print("Requested 'CMAP' ({!r}) cannot be found!".format(cmap))
        sys.exit()

    # Return cmap
    return(cmap)


# This function attempts to import a collection of packages with colormaps
def import_cmap_pkgs():
    # Define set of packages with colormaps
    cmap_pkgs = {'cmocean', 'colorcet', 'palettable'}

    # Obtain packages from CMR_CMAP_PKGS environment variable
    env_pkgs = os.environ.get('CMR_CMAP_PKGS', None)

    # Add env_pkgs to cmap_pkgs if it is not empty
    if env_pkgs is not None:
        # If Windows, split variable at semicolons
        if sys.platform.startswith('win'):
            env_pkgs = env_pkgs.split(';')
        # Else, if UNIX, split variable at colons
        elif sys.platform.startswith(('darwin', 'linux')):
            env_pkgs = env_pkgs.split(':')
        # Else, ignore the variable
        else:
            env_pkgs = []

        # Add pkgs
        cmap_pkgs.update(env_pkgs)

    # Attempt to import each package
    for cmap_pkg in cmap_pkgs:
        try:
            import_module(cmap_pkg)
        except ImportError:
            pass


# %% MAIN FUNCTION
def main():
    """
    This is the main function of the CLI and is called whenever `cmr` is
    invoked from the command-line.

    """

    # Initialize argparser
    parser = argparse.ArgumentParser(
        'cmr',
        description=main_desc,
        formatter_class=HelpFormatterWithSubCommands,
        add_help=True,
        allow_abbrev=True)

    # Add subparsers
    subparsers = parser.add_subparsers(
        title='commands',
        metavar='COMMAND')

    # OPTIONAL ARGUMENTS
    # Add 'version' argument
    parser.add_argument(
        '-v', '--version',
        action='version',
        version="CMasher v{}".format(__version__))

    # Create a cmap parser for several commands
    cmap_parent_parser = argparse.ArgumentParser(add_help=False)

    # Add 'cmap' argument
    cmap_parent_parser.add_argument(
        'cmap',
        help=("Name of colormap to use as registered in *matplotlib* or the "
              "object path of a colormap (e.g., 'a.b:c.d' -> import a.b; "
              "cmap = a.b.c.d)"),
        metavar='CMAP',
        action='store',
        type=str)

    # BIBTEX COMMAND
    # Add bibtex subparser
    bibtex_parser = subparsers.add_parser(
        'bibtex',
        description=e13.get_main_desc(cmr.get_bibtex),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Set defaults for bibtex_parser
    bibtex_parser.set_defaults(func=cli_bibtex)

    # CMAP_TYPE COMMAND
    # Add cmap_type subparser
    cmap_type_parser = subparsers.add_parser(
        'cmtype',
        parents=[cmap_parent_parser],
        description=e13.get_main_desc(cmr.get_cmap_type),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Set defaults for cmap_type_parser
    cmap_type_parser.set_defaults(func=cli_cmap_type)

    # CMAP_COLORS COMMAND
    # Obtain the optional default arguments of take_cmap_colors
    defaults = cmr.take_cmap_colors.__kwdefaults__

    # Create a take_colors parser
    take_colors_parent_parser = argparse.ArgumentParser(add_help=False)

    # Add 'cmap_range' optional argument
    take_colors_parent_parser.add_argument(
        '--range',
        help=("Normalized value range in the colormap from which colors should"
              " be taken"),
        metavar=('LOWER', 'UPPER'),
        action='store',
        nargs=2,
        default=defaults['cmap_range'],
        type=float,
        dest='cmap_range')

    # Add 'fmt' optional argument
    take_colors_parent_parser.add_argument(
        '--fmt',
        help="Format to return colors in",
        action='store',
        default=defaults['return_fmt'],
        choices=['float', 'norm', 'int', '8bit', 'str', 'hex'],
        type=str,
        dest='return_fmt')

    # Add cmap_colors subparser
    cmap_colors_parser = subparsers.add_parser(
        'cmcolors',
        parents=[cmap_parent_parser, take_colors_parent_parser],
        description=e13.get_main_desc(cmr.take_cmap_colors),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Add 'N' argument
    cmap_colors_parser.add_argument(
        'ncolors',
        help="Number of colors to take",
        metavar='N',
        action='store',
        type=int)

    # Set defaults for cmap_colors_parser
    cmap_colors_parser.set_defaults(func=cli_cmap_colors)

    # RGB_TABLE COMMAND
    # Add rgb_table subparser
    rgb_table_parser = subparsers.add_parser(
        'rgbtable',
        parents=[cmap_parent_parser, take_colors_parent_parser],
        description="Retrieves the RGB values of the provided `cmap`.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Set defaults for rgb_table_parser
    rgb_table_parser.set_defaults(func=cli_cmap_colors,
                                  ncolors=None)

    # MK_CMOD COMMAND
    # Add mk_cmod subparser
    mk_cmod_parser = subparsers.add_parser(
        'mkcmod',
        description=e13.get_main_desc(cmr.create_cmap_mod),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Add 'cmap' argument
    mk_cmod_parser.add_argument(
        'cmap',
        help="Name of *CMasher* colormap to create standalone module for",
        metavar='CMAP',
        action='store',
        type=str)

    # Add 'dir' optional argument
    mk_cmod_parser.add_argument(
        '-d', '--dir',
        help="Path to directory where the module must be saved",
        action='store',
        default=cmr.create_cmap_mod.__kwdefaults__['save_dir'],
        type=str)

    # Set defaults for mk_cmod_parser
    mk_cmod_parser.set_defaults(func=cli_mk_cmod)

    # Parse the arguments
    global ARGS
    ARGS = parser.parse_args()

    # If arguments is empty (no func was provided), show help
    if 'func' not in ARGS:
        parser.print_help()
    # Else, call the corresponding function
    else:
        ARGS.func()
