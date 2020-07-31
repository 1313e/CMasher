# -*- coding: utf-8 -*-

# %% IMPORTS
# Built-in imports
import argparse
from importlib import import_module
import sys

# Package imports
import e13tools as e13
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
                # If so, loop over all subcommands defined in the action
                for name, subparser in action.choices.items():
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
    print(cmr.get_cmap_type(ARGS.cmap))


# This function handles the 'take_cmap_colors' subcommand
def cli_take_cmap_colors():
    # Obtain the colors
    colors = cmr.take_cmap_colors(ARGS.cmap, ARGS.n_colors,
                                  cmap_range=ARGS.cmap_range,
                                  return_fmt=ARGS.return_fmt)

    # Print the colors line-by-line
    if ARGS.return_fmt in ('float', 'norm'):
        np.savetxt(sys.stdout, colors, '%.8f')
    elif ARGS.return_fmt in ('int', '8bit'):
        np.savetxt(sys.stdout, colors, '%i')
    else:
        np.savetxt(sys.stdout, colors, '%s')


# %% FUNCTION DEFINITIONS


# %% MAIN FUNCTION
def main():
    """
    This is the main function of the CLI and is called whenever `cmr` is
    invoked from the command-line.

    """

    # Define list of packages with colormaps
    cmap_pkgs = ['cmocean', 'colorcet', 'palettable']

    # Attempt to import each package
    for cmap_pkg in cmap_pkgs:
        try:
            import_module(cmap_pkg)
        except ImportError:
            pass

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
        help="Colormap to use",
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
        'cmap_type',
        parents=[cmap_parent_parser],
        description=e13.get_main_desc(cmr.get_cmap_type),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Set defaults for cmap_type_parser
    cmap_type_parser.set_defaults(func=cli_cmap_type)

    # TAKE_CMAP_COLORS COMMAND
    # Add take_cmap_colors subparser
    take_cmap_colors_parser = subparsers.add_parser(
        'take_cmap_colors',
        parents=[cmap_parent_parser],
        description=e13.get_main_desc(cmr.take_cmap_colors),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True)

    # Add 'N' argument
    take_cmap_colors_parser.add_argument(
        'n_colors',
        help="Number of colors to take",
        metavar='N',
        action='store',
        type=int)

    # Obtain the optional default arguments
    defaults = cmr.take_cmap_colors.__kwdefaults__

    # Add 'cmap_range' optional argument
    take_cmap_colors_parser.add_argument(
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
    take_cmap_colors_parser.add_argument(
        '--fmt',
        help="Format to return colors in",
        action='store',
        default=defaults['return_fmt'],
        choices=['float', 'norm', 'int', '8bit', 'hex', 'str'],
        type=str,
        dest='return_fmt')

    # Set defaults for take_cmap_colors_parser
    take_cmap_colors_parser.set_defaults(func=cli_take_cmap_colors)

    # Parse the arguments
    global ARGS
    ARGS = parser.parse_args()

    # If arguments is empty (no func was provided), show help
    if 'func' not in ARGS:
        parser.print_help()
    # Else, call the corresponding function
    else:
        ARGS.func()
