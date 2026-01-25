# [ main.py ] #

# Scripted by Invicta

# ======================== INFO ============================ #

# --- [CORE] ----------------------------------------------- #
# (checks.py): password check and score system
# (cli.py): handles terminal argument functionality
# (generator.py): generates password with given check mode
# (utils.py): helper and debugging functions

# --- [DATA] ----------------------------------------------- #
# (changelog.py): stores all past updates
# (data.py): holds sets, min requirements and such
# (save.py): saves check results to JSON file
# (stats.py): tracks and saves tool usage statistics

# --- [UI] ------------------------------------------------- #
# (menus.py): menus handler (each menu has its own submenu)
# (ui_logic.py): holds user input and menu logic functions
# (visuals.py): holds user interface constants 

# --- [/] -------------------------------------------------- #
# (__main__.py): main loop (wrapper for everything)

# ---------------------------------------------------------- #

# [Next Update]:
# < --- [CORE] --- >
# (cli.py): add multiple password check
# (generator.py): add 'multiple password generate' option
#
# < --- [DATA] --- >
# (save.py): improve save file json format
# (logging_config.py): implement consistent logging calls
#
# < ---- [UI] ---- >
# (menus.py): add stats menu

# ========================================================== #






# ======== Setup ======== #

# [ Libraries ] #
import os, time, logging
logger = logging.getLogger(__name__)

# [ Modules ] #
from .core.cli import parse_args
from .data.save import save_result
from .data.stats import load_stats, atomic_save_stats
from .core.checks import rate_password
from .core.generator import generate_password
from .ui.menus import display_main_menu, choose_menu, display_password_checker_menu, display_password_generator_menu, display_changelog_submenu, display_help_submenu
from .core.utils import DebugMsg, DebugInput, QuitTool, cmd_title, clr_scr, exit_msg






# ======== Main ======== #

def run_ui(user_stats: dict=None):
    """Run main user interface loop."""
    logger.info("'run_ui' executed.")
    
    user_stats["starts"] += 1
    user_stats["last_used"] = time.strftime("%Y-%m-%d - %H:%M:%S")
    if user_stats["first_used"] is None: user_stats["first_used"] = user_stats["last_used"]
    
    current_session_start_time = time.perf_counter()

    try:
        while True:
            # main loop
            logger.info("User in home menu")
            cmd_title("password_checker_py - Home")
            display_main_menu(True, True)
            wish_menu = choose_menu(easter_egg=True, submenu="Home")

            if wish_menu == 0:
                # stay
                continue

            elif wish_menu == 1:
                logger.info("Loading checker menu...")
                cmd_title("password_checker_py - Check")
                display_password_checker_menu(True, user_stats=user_stats)

            elif wish_menu == 2:
                logger.info("Loading generator menu...")
                cmd_title("password_checker_py - Generate")
                display_password_generator_menu(True, user_stats=user_stats)

            elif wish_menu == 3:
                # changelog menu
                logger.info("Loading changlog menu...")
                cmd_title("password_checker_py - Changelog")
                display_changelog_submenu()

            elif wish_menu == 4:
                # help menu
                logger.info("Loading help menu...")
                cmd_title("password_checker_py - Help")
                display_help_submenu()

            elif wish_menu == 9:
                # quit
                logger.info("Quitting tool...")
                os.system('title')
                clr_scr()
                print(exit_msg)
                break

            else:
                # consider as stay
                logger.info("User typed invalid input: main menu")
                DebugInput("warn", "Invalid option: please input an available menu", True, True)
                continue

    except Exception as e:
        logger.warning("Exception triggered: %s", e)
        clr_scr()
        DebugMsg("error", "An unexpected error occured: 'main' in '__main__.py'.", False, True)
        QuitTool()
    
    finally:
        # always tracks session time
        elapsed = time.perf_counter() - current_session_start_time
        user_stats["total_sessions_seconds"] += elapsed

        atomic_save_stats(user_stats)


def main():
    """Main 'password_checker_py' program."""
    
    # stats handling
    stats = load_stats()
    
    # argument handling
    args = parse_args(user_stats=stats)

    if args is None:
        run_ui(user_stats=stats)
        return
    if args.log or args.verbose:
        run_ui(user_stats=stats)
        return
    
    if args.password is not None:
        res = rate_password(args.password, args.check_mode, False)
        rescalc = res[2]
        #finalres = f"{rescalc:.2f}"
        print(f"Score: {rescalc}")
        if args.output:
            save_result(args.password, args.check_mode, rescalc, res[1], args.output)
    
    elif args.generate is not None:
        pwd = generate_password(args.check_mode, False, user_stats=stats)
        print(f"Generated password: {pwd}")
        print(f"Score: {rate_password(pwd, args.check_mode, False)[2]}")
        if args.output:
            save_result(pwd, args.check_mode, rate_password(pwd, args.check_mode, False)[2], rate_password(pwd, args.check_mode, False)[1], args.output)






if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt")
        try:
            QuitTool()
        except SystemExit:
            os._exit(130)
