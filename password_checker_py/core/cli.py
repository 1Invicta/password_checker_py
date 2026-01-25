# [ cli.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import sys, argparse, logging
from pathlib import Path

# [ Modules ] #
from ..data.changelog import changelog
from ..data.logging_config import setup_logging

# [ Information ] #
LATEST_UPDATE = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]

# [ Helper ] #
def display_version_info():
    newline = "\n"
    print(f"{newline} Current version: [{LATEST_UPDATE}]")
    print(f" Last updated on: [{LATEST_UPDATE_DATE}]")

def display_user_stats(user_stats: dict=None):
    session_time_minutes = f"{int(user_stats["total_sessions_seconds"]// 60)}"
    session_time_seconds = f"{int(user_stats["total_sessions_seconds"] % 60)}"
    total_session_time = session_time_minutes+"m" + session_time_seconds+"s"
    newline = "\n"
    
    print(f"{newline}-> First used:              {user_stats["first_used"]}")
    print(f" * Tool starts:             {user_stats["starts"]:,}")
    print(f" * Total session time:      {total_session_time}")
    print(f" * Passwords tested:        {user_stats["passwords_tested"]:,}")
    
    if user_stats["passwords_tested"] > 0:
        avg_len = user_stats["total_length_sum"] / user_stats["passwords_tested"]
        print(f" * Average password length: {avg_len:.1f} characters")
    else: print(f" * Average password length: ---")
    
    print(f" * Passwords generated:     {user_stats["passwords_generated"]}")
    print(f"{newline}-> Last used:               {user_stats["last_used"]}")


# ======== Parse ======== #

def parse_args(user_stats=None):
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
        "-s", "--stats",
        action="store_true",
        help="Display tool usage statistics"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Display version information"
    )

    parser.add_argument(
        "-l", "--log", 
        action="store_true", 
        help="Write log file")
    parser.add_argument("--log-dir", default=Path(__file__).parent.parent / "data" /"logs")
    parser.add_argument(
        "--verbose", 
        action="store_true",
        help="Enable debug-level logging (requires --log)")

    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output results to a JSON (JSONL) file"
    )

    args = parser.parse_args()
    level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(
        log_to_file=args.log,
        log_dir=args.log_dir,
        level=level
    )
    logger = logging.getLogger(__name__)
    logger.info("Logging system initialised.")

    # ------------------------------ #
    #      MUTUAL REQUIREMENTS       #
    # ------------------------------ #
    if args.version:
        display_version_info()
        sys.exit(0)
    
    if args.stats:
        display_user_stats(user_stats)
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

