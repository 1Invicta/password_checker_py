# [ cli.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import          sys
import      argparse
import       logging

logger = logging.getLogger(__name__)

from pathlib import Path

# [ Modules ] #
from ..data.changelog           import changelog
from ..data.logging_config      import setup_logging

# [ Information ] #
LATEST_UPDATE = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]

# [ Helper ] #
def display_version_info():
    """Displays the tool's current version."""

    logger.info("'display_version_info' executed.")

    newline = "\n"

    print("\n [password_checker_py]")
    print(f"{newline}  * Current version: [{LATEST_UPDATE}]")
    print(f"  * Last updated on: [{LATEST_UPDATE_DATE}]")
    print("\n >> A tool created and developed by 1Invicta <<")


def display_user_stats( user_stats: dict=None ):
    """Displays user statistics."""

    logger.info("'display_user_stats' executed.")

    newline = "\n"
    
    total_minutes = user_stats["total_sessions_seconds"] // 60
    seconds_remainder = user_stats["total_sessions_seconds"] % 60
    total_session_time = f"{int(total_minutes)}m{int(seconds_remainder)}s"
    

    first_used = user_stats["first_used"]
    starts = user_stats["starts"]
    passwords_tested = user_stats["passwords_tested"]
    passwords_generated = user_stats["passwords_generated"]
    last_used = user_stats["last_used"]
    

    print(f"{newline}-> First used:              {first_used}")
    print(f" * Tool starts:             {starts:,}")
    print(f" * Total session time:      {total_session_time}")
    print(f" * Passwords tested:        {passwords_tested:,}")
    
    if user_stats["passwords_tested"] > 0:
        avg_len = user_stats["total_length_sum"] / user_stats["passwords_tested"]
        print(f" * Average password length: {avg_len:.1f} characters")
    
    else:
        print(f" * Average password length: ---")
    
    print(f" * Passwords generated:     {passwords_generated}")
    print(f"{newline}-> Last used:               {last_used}")




# ======== Parse ======== #

def new_parse_args( user_stats=None ):

    parser = argparse.ArgumentParser(
        prog="password_checker_py",
        description="Password checker & generator"
    )

    # ===== GLOBAL FLAGS =====
    parser.add_argument(
        "-l", "--log",
        action="store_true",
        help="Write log file"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug-level logging (requires --log)"
    )

    parser.add_argument(
        "--log-dir",
        default=Path(__file__).parent.parent / "data" / "logs"
    )

    # ===== SUBPARSERS =====
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ===== CHECK =====
    check_parser = subparsers.add_parser("check", help="Check password(s)")
    check_parser.add_argument("-m", "--check-mode", type=int, choices=[1, 2, 3], required=True)

    group = check_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--password", type=str)
    group.add_argument("-f", "--file", type=str)

    check_parser.add_argument("-o", "--output", type=str)

    # ==== GENERATE ====
    gen_parser = subparsers.add_parser("generate", help="Generate password(s)")
    gen_parser.add_argument("-m", "--check-mode", type=int, choices=[1, 2, 3], required=True)
    gen_parser.add_argument("-c", "--count", type=int, default=1)
    gen_parser.add_argument("-o", "--output", type=str)

    # ===== STATS =====
    subparsers.add_parser("stats", help="Display statistics")

    # ===== VERSION =====
    subparsers.add_parser("version", help="Display version")

    # ===== RUN =====
    run_parser = subparsers.add_parser("run", help="Run program with user interface")
    
    args = parser.parse_args()

    # ===== SETUP LOGGING AFTER PARSING =====
    level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(
        log_to_file=args.log,
        log_dir=args.log_dir,
        level=level
    )

    logging.getLogger(__name__).info("Logging system initialised.")

    return args
