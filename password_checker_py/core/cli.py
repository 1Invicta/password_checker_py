# [ cli.py ]


# ======== Setup ======== #

# [ Libraries ]
import sys, argparse
#from colorama import Fore, Style

# [ Modules ]
from ..data.changelog import changelog
#from .utils import display_latest_update

LATEST_UPDATE = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]


def display_version_info():
    print(f"\n Current version: [{LATEST_UPDATE}]")
    print(f" Last updated on: [{LATEST_UPDATE_DATE}]")



# ======== Parse ======== #

def parse_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="password_checker_py",
        description="Password checker & generator"
    )

    parser.add_argument(
        "-p", "--password",
        type=str,
        help="Password to check"
    )


    parser.add_argument(
        "-cm", "--check-mode",
        type=int,
        choices=[1, 2, 3],
        help="Mode to use (1, 2 or 3)"
    )

    parser.add_argument(
        "-g", "--generate",
        action="store_true",
        help="Generate a password"
    )

    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Display version information"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output results to a JSON file"
    )

    args = parser.parse_args()

    # ------------------------------ #
    #      MUTUAL REQUIREMENTS       #
    # ------------------------------ #
    if args.version:
        #display_latest_update(LATEST_UPDATE_DATE, LATEST_UPDATE, True)
        #print(f"\n [ver-{LATEST_UPDATE}] - {LATEST_UPDATE_DATE}")
        display_version_info()
        sys.exit(0)
    
    if len(sys.argv) == 1:
        return None
    
    # password checking
    if args.password:
        if args.generate:
            parser.error("Cannot use '--password' and '--generate' at the same time.")
        if args.check_mode is None:
            parser.error("Using '--password' requires '--check-mode'.")
        return args
    
    # generate password
    if args.generate:
        if args.password:
            parser.error("Cannot use '--generate' and '--password' at the same time.")
        if args.check_mode is None:
            parser.error("Using '--generate' requires '--check-mode'.")
        return args
    
    if args.check_mode:
        if args.password is None or args.generate is None:
            parser.error("Using '--check-mode' requires '--password' or '--generate'.")
    
    return args

