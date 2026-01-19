# [ main.py ] #

# Scripted by Invicta

# ======================== INFO ============================ #

# --- [CORE] ----------------------------------------------- #
# (checks.py): password check and score system
# (cli.py): handles terminal argument functionality
# (generator.py): generates password with given check mode
# (utils.py): helper and debugging functions
# (variables.py): holds global variables and constants

# --- [DATA] ----------------------------------------------- #
# (changelog.py): stores all past updates
# (save.py): saves check results to JSON file

# --- [UI] ------------------------------------------------- #
# (menus.py): menus handler (each menu has its own submenu)
# (visuals.py): holds CLI user interface constants

# --- [/] -------------------------------------------------- #
# (__main__.py): main loop (wrapper for everything)

# ========================================================== #








# ======== Setup ======== #

# [ Libraries ] #
import os

# [ Modules ] #
from .core.cli import parse_args
from .data.save import save_result
from .core.checks import rate_password
from .core.generator import generate_password
from .ui.menus import display_main_menu, choose_menu, display_password_checker_menu, display_password_generator_menu, display_changelog_submenu, display_help_submenu
from .core.utils import DebugMsg, DebugInput, QuitTool, cmd_title, clr_scr, exit_msg






# ======== Main ======== #

def run_ui():
    """Run main user interface loop."""
    try:
        while True:
            cmd_title("password_checker_py - Home")
            # main loop
            display_main_menu(True)
            wish_menu = choose_menu(easter_egg=True, submenu="Home")

            if wish_menu == 0:
                # stay
                continue

            elif wish_menu == 1:
                cmd_title("password_checker_py - Check")
                display_password_checker_menu(True)

            elif wish_menu == 2:
                cmd_title("password_checker_py - Generate")
                display_password_generator_menu(True)

            elif wish_menu == 3:
                cmd_title("password_checker_py - Changelog")
                # changelog menu
                display_changelog_submenu()

            elif wish_menu == 4:
                cmd_title("password_checker_py - Help")
                # help menu
                display_help_submenu()

            elif wish_menu == 9:
                os.system('title')
                # quit
                clr_scr()
                print(exit_msg)
                break

            else:
                # consider as stay
                DebugInput("warn", "Invalid option: please input an available menu", True, True)
                continue

    except Exception:
        clr_scr()
        DebugMsg("error", "An unexpected error occured: 'main' in '__main__.py'.", False, True)
        QuitTool()


def main():
    """Main 'password_checker_py' program."""
    args = parse_args()

    if args is None:
        run_ui()
        return
    
    if args.password is not None: # type: ignore
        res = rate_password(args.password, args.check_mode, False) # type: ignore
        rescalc = res[2]
        #finalres = f"{rescalc:.2f}"
        print(f"Score: {rescalc}")
        if args.output:
            save_result(args.password, args.check_mode, rescalc, res[1], args.output)
    
    elif args.generate is not None: # type: ignore
        pwd = generate_password(args.check_mode, False) # type: ignore
        print(f"Generated password: {pwd}")
        print(f"Score: {rate_password(pwd, args.check_mode, False)[2]}")
        if args.output:
            save_result(pwd, args.check_mode, rate_password(pwd, args.check_mode, False)[2], rate_password(pwd, args.check_mode, False)[1], args.output)

    




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            QuitTool()
        except SystemExit:
            os._exit(130)
