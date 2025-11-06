# [ main.py ] #


# ========================= NOTES ========================== #

# (variables.py): holds global variables and constants
# (visuals.py): holds CLI user interface constants
# (utils.py): helper and debugging functions
# (checks.py): password check and score system
# (menus.py): menus handler (each menu has its own submenu)
# (changelog.py): stores all past updates
# (main.py): main loop (wrapper for everything)

# ========================================================== #



# FUTURE (ver-0.4.0):
# [/] - implement OOP for (checks.py)

# [ Libraries ] #
import os

# [ Modules ] #
from ui.menus import display_main_menu, choose_menu, display_password_checker_menu, display_changelog_submenu, display_help_submenu
from core.utils import DebugMsg, DebugInput, QuitTool, cmd_title, clr_scr, exit_msg

# [ Main ] #
def main():
    """Main 'password_checker_py' program."""
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
                cmd_title("password_checker_py - Changelog")
                # changelog menu
                display_changelog_submenu()

            elif wish_menu == 3:
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
        DebugMsg("error", "An unexpected error occured: 'main' in 'main.py'.", False, True)
        QuitTool()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            QuitTool()
        except SystemExit:
            # retries if failed
            os._exit(130)
