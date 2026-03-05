# [ main.py ] #


# A tool created and developed and maintained by Invicta

# ======================== INFO ============================ #

# --- [CORE] ----------------------------------------------- #
# /checks.py/       password check and score system          #
# /cli.py/          handles terminal argument functionality  #
# /generator.py/    generates password with given check mode #
# /utils.py/        helper and debugging functions           #


# --- [DATA] ----------------------------------------------- #
# /changelog.py/   stores all past updates                   #
# /data.py/        holds sets, min requirements and such     #
# /save.py/        saves check results to JSON (JSONL) file  #
# /stats.py/       tracks and saves tool usage statistics    #


# --- [UI] ------------------------------------------------- #
# /menus.py/       menus handler (each menu has its submenu) #
# /ui_logic.py/    holds user input and menu logic functions #
# /visuals.py/     holds user interface constants            #


# --- [/] -------------------------------------------------- #
# /__main__.py/    main loop (wrapper for everything)        #


# ---------------------------------------------------------- #


# [Next Update] -------------------------------------------- #
# < --- [CORE] --- >                                         #
# /cli.py/         add multiple password check               #
# /ALL/            consider prefix naming convention         #

# ========================================================== #






# ======== Setup ======== #

# [ Libraries ] #
import          sys
import         time
import      logging

logger = logging.getLogger(__name__)

# [ Modules ] #
from .core.cli          import parse_args, new_parse_args, display_user_stats, display_version_info
from .data.stats        import load_stats, atomic_save_stats
from .core.processing   import process_check, process_generate
from .core.utils        import DebugMsg, DebugInput, QuitTool, cmd_title, clr_scr, exit_msg
from .ui.menus import (
    display_main_menu, choose_menu, display_password_checker_menu,
    display_password_generator_menu, display_changelog_submenu, 
    display_help_submenu, display_info_submenu
)






# ======== Main ======== #

def run_ui( user_stats: dict=None ):
    """Run main user interface loop."""
    
    logger.info("'run_ui' executed.")
    
    user_stats["starts"] += 1
    user_stats["last_used"] = time.strftime("%Y-%m-%d - %H:%M:%S")
    
    if user_stats["first_used"] is None: user_stats["first_used"] = user_stats["last_used"]

    try:
        # MAIN LOOP
        while True:
            logger.info("User in home menu")
            cmd_title("password_checker_py - Home")
            display_main_menu(True, True, user_stats=user_stats)
            wish_menu = choose_menu(easter_egg=True, submenu="Home")

            if wish_menu == 0:
                continue

            elif wish_menu == 1:
                logger.info("Loading checker menu...")
                cmd_title("password_checker_py - Check")
                display_password_checker_menu(user_stats=user_stats)

            elif wish_menu == 2:
                logger.info("Loading generator menu...")
                cmd_title("password_checker_py - Generate")
                display_password_generator_menu(user_stats=user_stats)

            elif wish_menu == 3:
                logger.info("Loading changlog menu...")
                cmd_title("password_checker_py - Changelog")
                display_changelog_submenu(user_stats=user_stats)

            elif wish_menu == 4:
                logger.info("Loading help menu...")
                cmd_title("password_checker_py - Help")
                display_help_submenu(user_stats=user_stats)
            
            elif wish_menu == 5:
                logger.info("Loading info menu...")
                cmd_title("password_checker_py - Info")
                display_info_submenu(stats=user_stats)

            elif wish_menu == 9:
                logger.info("Quitting tool...")
                cmd_title('')
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
        # always save updated user stats
        atomic_save_stats(user_stats)


def main():
    """Main 'password_checker_py' program."""
    
    logger.info("'main' executed.")
    from colorama import init
    init(autoreset=True)
    
    stats = load_stats()
    #args = parse_args(user_stats=stats)
    args = new_parse_args(user_stats=stats)

    if args.command == "check":
        process_check(args, stats)
    
    elif args.command == "generate":
        process_generate(args, stats)

    elif args.command == "stats":
        display_user_stats(stats)
    
    elif args.command == "version":
        display_version_info()
    
    elif args.command == "run":
        run_ui(stats)






if __name__ == "__main__":
    
    try:
        main()

    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt")
        
        try:
            QuitTool()
        
        except SystemExit:
            sys.exit(1)
