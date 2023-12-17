# %% IMPORTS
# Built-in imports
import argparse
import os
import re
import sys
from importlib import import_module
from textwrap import dedent

# Package imports
import matplotlib as mpl
import numpy as np

import cmasher as cmr

# CMasher imports
from cmasher import __version__

# All declaration
__all__ = ["main"]


# %% GLOBALS
# Define set of packages with colormaps
cmap_pkgs = {"cmocean", "colorcet", "palettable"}

# Define main description of this package
main_desc = dedent(
    """
    CMasher: Scientific colormaps for making accessible, informative and
    'cmashing' plots"""
)[1:]
main_epilog = dedent(
    """
    This CLI-tool provides access to several of CMasher's utility functions.
    As several commands require a colormap object to work, all Python packages
    defined in the 'CMR_CMAP_PKGS' environment variable in addition to the
    following packages %s are attempted to be imported before any command is
    executed."""
)[1:] % (tuple(cmap_pkgs),)


def _get_main_desc(source):
    """
    Retrieves the main description of the provided object `source` and returns
    it.

    The main description is defined as the first paragraph of its docstring.

    Parameters
    ----------
    source : object
        The object whose main description must be retrieved.

    Returns
    -------
    main_desc : str or None
        The main description string of the provided `source` or *None* if
        `source` has not docstring.

    """
    # this function is copied from the e13tools package

    # Retrieve the docstring of provided source
    doc = source.__doc__

    # If doc is None, return None
    if doc is None:
        return None

    # Obtain the index of the last character of the first paragraph
    index = doc.find("\n\n")

    # If index is -1, there is only 1 paragraph
    if index == -1:
        index = len(doc)

    # Gather everything up to this index
    doc = doc[:index]

    # Replace all occurrences of 2 or more whitespace characters by a space
    doc = re.sub(r"\s{2,}", " ", doc)

    # Return doc
    return doc.strip()


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
                    self._add_item(
                        self.format_subcommands, [name, subparser.description]
                    )
            # Call super method in all other cases
            else:
                super().add_argument(action)

    # This function formats the description of a subcommand with given name
    def format_subcommands(self, name, description):
        # Determine the positions and widths of the help texts
        help_position = min(self._action_max_length + 2, self._max_help_position)
        help_width = max(self._width - help_position, 11)
        name_width = help_position - self._current_indent - 2

        # Transform name to the proper formatting
        name = "{0}{1: <{2}}{3}".format(
            " " * self._current_indent,
            name,
            name_width,
            "  " if (len(name) <= name_width) else "\n" + " " * help_position,
        )

        # Split the lines of the subcommand description
        desc_lines = self._split_lines(description, help_width)

        # Create list of all parts of the description of this subcommand
        parts = [name, desc_lines.pop(0), "\n"]

        # Loop over all remaining desc_lines
        for line in desc_lines:
            # Format and add to parts
            parts.append(f"{' '*help_position}{line}\n")

        # Convert to a single string and return
        return "".join(parts)


# %% COMMAND FUNCTION DEFINITIONS
# This function handles the 'bibtex' subcommand
def cli_bibtex():
    cmr.get_bibtex()


# This function handles the 'cmlist' subcommand
def cli_cmlist():
    # Obtain list without reversed versions
    cmaps = [
        cmap for cmap in cmr.get_cmap_list(ARGS.cmap_type) if not cmap.endswith("_r")
    ]

    # Create string with all cmaps
    cmaps_str = "\n".join(cmaps)

    # Print string
    print(cmaps_str)


# This function handles the 'cmtype' subcommand
def cli_cmap_type():
    # Import cmap packages
    import_cmap_pkgs()

    # Print cmap type
    print(cmr.get_cmap_type(get_cmap(ARGS.cmap)))


# This function handles the 'cmcolors' subcommand
def cli_cmap_colors():
    # Import cmap packages
    import_cmap_pkgs()

    # Obtain the colors
    colors = cmr.take_cmap_colors(
        get_cmap(ARGS.cmap),
        ARGS.ncolors,
        cmap_range=ARGS.cmap_range,
        return_fmt=ARGS.return_fmt,
    )

    # Print the colors line-by-line
    if ARGS.return_fmt in ("float", "norm"):
        np.savetxt(sys.stdout, colors, "%.8f")
    elif ARGS.return_fmt in ("int", "8bit"):
        np.savetxt(sys.stdout, colors, "%i")
    else:
        np.savetxt(sys.stdout, colors, "%s")


# This function handles the 'mkcmod' subcommand
def cli_mk_cmod():
    # Loop over all cmaps in ARGS.cmap
    for cmap in ARGS.cmap:
        # Create stand_alone module for this cmap
        cmap_path = cmr.create_cmap_mod(cmap, save_dir=ARGS.dir)

        # Print on commandline that module has been created
        print(f"Created standalone colormap module of {cmap} as {cmap_path}.")


# This function handles the 'cmview' subcommand
def cli_cmap_view():
    # Import cmap packages
    import_cmap_pkgs()

    # View cmap
    save = ARGS.cmap + ".png" if ARGS.save is True else ARGS.save
    cmr.view_cmap(
        get_cmap(ARGS.cmap), savefig=save, show_test=ARGS.test, show_grayscale=ARGS.gs
    )


# This function handles the 'app_usage tableau' subcommand
def cli_app_usage_tableau():
    # Create/Update Tableau properties file
    cmr.app_usage.update_tableau_pref_file(dirname=ARGS.dir)

    # Print on commandline that properties file was created/updated
    print(
        "Created/Updated Tableau preferences file in %r." % (os.path.abspath(ARGS.dir))
    )


# This function handles the 'lang_usage r' subcommand
def cli_lang_usage_r():
    # Print on commandline to look this up on the CMasher docs
    print(
        "Please see <https://cmasher.readthedocs.io/user/lang_usage/R.html> "
        "for instructions on how to access *CMasher* colormaps in *R*."
    )


# %% FUNCTION DEFINITIONS
# This function obtains the colormap that was requested
def get_cmap(cmap):
    # Try to obtain the colormap from MPL
    try:
        cmap = mpl.colormaps[cmap]

    # If this does not work, try to expand given cmap in setuptools-style
    except ValueError:
        # Check if cmap contains a colon
        if ":" in cmap:
            # Split cmap up into mod_name and obj_name
            mod_name, obj_name = cmap.split(":", 1)
            obj_path = obj_name.split(".")

            # Import the provided module as cmap
            cmap = import_module(mod_name)

            # Import the provided object from this module
            for obj in obj_path:
                cmap = getattr(cmap, obj)

    # If cmap is still a string, raise error
    if isinstance(cmap, str):
        # Print error and exit
        print(f"Requested 'CMAP' ({cmap!r}) cannot be found!")
        sys.exit()

    # Return cmap
    return cmap


# This function attempts to import a collection of packages with colormaps
def import_cmap_pkgs():
    # Obtain packages from CMR_CMAP_PKGS environment variable
    env_pkgs = os.environ.get("CMR_CMAP_PKGS", None)

    # Add env_pkgs to cmap_pkgs if it is not empty
    if env_pkgs is not None:
        # If Windows, split variable at semicolons
        if sys.platform.startswith("win"):
            env_pkgs = env_pkgs.split(";")
        # Else, if UNIX, split variable at colons
        elif sys.platform.startswith(("darwin", "linux")):
            env_pkgs = env_pkgs.split(":")
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


# This function adds the app_usage parser
def add_app_usage_parser(main_subparsers):
    # APP_USAGE COMMAND
    # Add app_usage parser
    parser = main_subparsers.add_parser(
        "app_usage",
        description=(
            "Access various function definitions useful for porting "
            "*CMasher* colormaps to other applications."
        ),
        formatter_class=HelpFormatterWithSubCommands,
        add_help=True,
    )

    # Set defaults for this parser
    parser.set_defaults(func="app_usage")

    # Create app_usage subparsers for app_usage parser
    subparsers = parser.add_subparsers(title="Applications", metavar="APP")

    # TABLEAU SUB-COMMAND
    # Add tableau subparser
    tableau_parser = subparsers.add_parser(
        "tableau",
        description=_get_main_desc(cmr.app_usage.update_tableau_pref_file),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Add 'dir' optional argument
    tableau_parser.add_argument(
        "-d",
        "--dir",
        help=(
            "Path to directory where the Tableau preferences file should be "
            "updated or created if it does not exist there."
        ),
        action="store",
        default=cmr.app_usage.update_tableau_pref_file.__defaults__[0],
        type=str,
    )

    # Set default for tableau parser
    tableau_parser.set_defaults(func=cli_app_usage_tableau)

    # Return parser
    return parser


# This function adds the lang_usage parser
def add_lang_usage_parser(main_subparsers):
    # LANG_USAGE COMMAND
    # Add lang_usage parser
    parser = main_subparsers.add_parser(
        "lang_usage",
        description=(
            "Access various function definitions useful for porting "
            "*CMasher* colormaps to other languages."
        ),
        formatter_class=HelpFormatterWithSubCommands,
        add_help=True,
    )

    # Set defaults for this parser
    parser.set_defaults(func="lang_usage")

    # Create lang_usage subparsers for lang_usage parser
    subparsers = parser.add_subparsers(title="Languages", metavar="LANG")

    # R SUB-COMMAND
    # Add tableau subparser
    r_parser = subparsers.add_parser(
        "r",
        description=(
            "Prints a URL to the online docs that describes how to "
            "access *CMasher* colormaps in *R*."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Set default for tableau parser
    r_parser.set_defaults(func=cli_lang_usage_r)

    # Return parser
    return parser


# %% MAIN FUNCTION
def main():
    """
    This is the main function of the CLI and is called whenever `cmr` is
    invoked from the command-line.

    """
    # Initialize argparser
    parser = argparse.ArgumentParser(
        "cmr",
        description=main_desc,
        epilog=main_epilog,
        formatter_class=HelpFormatterWithSubCommands,
        add_help=True,
        allow_abbrev=True,
    )

    # Add subparsers
    subparsers = parser.add_subparsers(title="commands", metavar="COMMAND")

    # OPTIONAL ARGUMENTS
    # Add 'version' argument
    parser.add_argument(
        "-v", "--version", action="version", version=f"CMasher v{__version__}"
    )

    # Create a cmap parser for several commands
    cmap_parent_parser = argparse.ArgumentParser(add_help=False)

    # Add 'cmap' argument
    cmap_parent_parser.add_argument(
        "cmap",
        help=(
            "Name of colormap to use as registered in *matplotlib* or the "
            "object path of a colormap (e.g., 'a.b:c.d' -> import a.b; "
            "cmap = a.b.c.d)."
        ),
        metavar="CMAP",
        action="store",
        type=str,
    )

    # BIBTEX COMMAND
    # Add bibtex subparser
    bibtex_parser = subparsers.add_parser(
        "bibtex",
        description=_get_main_desc(cmr.get_bibtex),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Set defaults for bibtex_parser
    bibtex_parser.set_defaults(func=cli_bibtex)

    # CMLIST COMMAND
    # Add cmlist subparser
    cmlist_parser = subparsers.add_parser(
        "cmlist",
        description=(
            "Prints a list of all colormaps available in *CMasher*. "
            "Reversed versions are excluded from this list."
        ),
        epilog=(
            "Note that *CMasher* colormaps registered in *MPL* have an "
            "added 'cmr.' prefix."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Add 'type' optional argument
    cmlist_parser.add_argument(
        "--type",
        help="Which colormap type to print.",
        action="store",
        default=cmr.get_cmap_list.__defaults__[0],
        choices=[
            "all",
            "s",
            "seq",
            "sequential",
            "d",
            "div",
            "diverging",
            "c",
            "cyc",
            "cyclic",
        ],
        type=str,
        dest="cmap_type",
    )

    # Set defaults for cmlist_parser
    cmlist_parser.set_defaults(func=cli_cmlist)

    # CMAP_TYPE COMMAND
    # Add cmap_type subparser
    cmap_type_parser = subparsers.add_parser(
        "cmtype",
        parents=[cmap_parent_parser],
        description=_get_main_desc(cmr.get_cmap_type),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Set defaults for cmap_type_parser
    cmap_type_parser.set_defaults(func=cli_cmap_type)

    # CMAP_COLORS COMMAND
    # Obtain the optional default arguments of take_cmap_colors
    defaults = cmr.take_cmap_colors.__kwdefaults__

    # Create a take_colors parser
    take_colors_parent_parser = argparse.ArgumentParser(add_help=False)

    # Add 'cmap_range' optional argument
    take_colors_parent_parser.add_argument(
        "--range",
        help=(
            "Normalized value range in the colormap from which colors should"
            " be taken."
        ),
        metavar=("LOWER", "UPPER"),
        action="store",
        nargs=2,
        default=defaults["cmap_range"],
        type=float,
        dest="cmap_range",
    )

    # Add 'fmt' optional argument
    take_colors_parent_parser.add_argument(
        "--fmt",
        help="Format to return colors in.",
        action="store",
        default=defaults["return_fmt"],
        choices=["float", "norm", "int", "8bit", "str", "hex"],
        type=str,
        dest="return_fmt",
    )

    # Add cmap_colors subparser
    cmap_colors_parser = subparsers.add_parser(
        "cmcolors",
        parents=[cmap_parent_parser, take_colors_parent_parser],
        description=_get_main_desc(cmr.take_cmap_colors),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Add 'N' argument
    cmap_colors_parser.add_argument(
        "ncolors",
        help="Number of colors to take.",
        metavar="N",
        action="store",
        type=int,
    )

    # Set defaults for cmap_colors_parser
    cmap_colors_parser.set_defaults(func=cli_cmap_colors)

    # RGB_TABLE COMMAND
    # Add rgb_table subparser
    rgb_table_parser = subparsers.add_parser(
        "rgbtable",
        parents=[cmap_parent_parser, take_colors_parent_parser],
        description="Retrieves the RGB values of the provided `cmap`.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Set defaults for rgb_table_parser
    rgb_table_parser.set_defaults(func=cli_cmap_colors, ncolors=None)

    # CMVIEW COMMAND
    # Add cmap_view subparser
    cmap_view_parser = subparsers.add_parser(
        "cmview",
        parents=[cmap_parent_parser],
        description=_get_main_desc(cmr.view_cmap),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Add 'save' optional argument
    cmap_view_parser.add_argument(
        "--save",
        help="Path where plot must be saved to.",
        metavar="PATH",
        action="store",
        nargs="?",
        default=None,
        const=True,
        type=str,
    )

    # Add 'test' optional argument
    cmap_view_parser.add_argument(
        "--test", help="Show a colormap test of `cmap` instead.", action="store_true"
    )

    # Add 'test' optional argument
    cmap_view_parser.add_argument(
        "--gs",
        "--grayscale",
        help="Show grayscale version of `cmap` as well.",
        action="store_true",
    )

    # Set defaults for cmap_view_parser
    cmap_view_parser.set_defaults(func=cli_cmap_view)

    # MK_CMOD COMMAND
    # Add mk_cmod subparser
    mk_cmod_parser = subparsers.add_parser(
        "mkcmod",
        description=_get_main_desc(cmr.create_cmap_mod),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=True,
    )

    # Add 'cmap' argument
    mk_cmod_parser.add_argument(
        "cmap",
        help="Name of *CMasher* colormap(s) to create standalone module for.",
        metavar="CMAP",
        action="store",
        nargs="+",
        type=str,
    )

    # Add 'dir' optional argument
    mk_cmod_parser.add_argument(
        "-d",
        "--dir",
        help="Path to directory where the module must be saved.",
        action="store",
        default=cmr.create_cmap_mod.__kwdefaults__["save_dir"],
        type=str,
    )

    # Set defaults for mk_cmod_parser
    mk_cmod_parser.set_defaults(func=cli_mk_cmod)

    # APP_USAGE COMMAND
    # Add app_usage parser
    app_usage_parser = add_app_usage_parser(subparsers)

    # LANG_USAGE COMMAND
    # Add lang_usage parser
    lang_usage_parser = add_lang_usage_parser(subparsers)

    # Parse the arguments
    global ARGS
    ARGS = parser.parse_args()

    # If arguments is empty (no func was provided), show help
    if "func" not in ARGS:
        parser.print_help()
    # Else if 'func' is 'app_usage', show help of 'app_usage' parser
    elif ARGS.func == "app_usage":
        app_usage_parser.print_help()
    # Else if 'func' is 'lang_usage', show help of 'lang_usage' parser
    elif ARGS.func == "lang_usage":
        lang_usage_parser.print_help()
    # Else, call the corresponding function
    else:
        ARGS.func()
