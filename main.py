### [main] ###

## /_NOTES/ ##
# (main.py) main loop => wrapper for everything
# (menus.py) menus handler => each menu has its own submenu
# (changelog.py) stores all past updates
# (checker.py) password check system
# (utils.py) helper and debugging functions

# FUTURE (ver-0.3.2):
# [/] - improve password checks, make them more rigorous
# [/] - refactor 'display_password_checker_menu' function!!!

# --- Mods --- #
from menus import *
from utils import DebugMsg, QuitTool, exit_msg

# --- Main --- #
def main():
    try:
        while True:
            # main loop
            display_main_menu(True)
            wish_menu = choose_menu()

            if wish_menu == 0:
                # stay
                continue

            elif wish_menu == 1:
                display_password_checker_menu(True)

            elif wish_menu == 2:
                # changelog menu
                display_changelog_submenu()

            elif wish_menu == 3:
                # info menu
                display_help_submenu()

            elif wish_menu == 9:
                # quit
                clr_scr()
                print(exit_msg)
                break

            else:
                # consider as stay
                DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                input("Type Enter to continue...")
                continue
    except:
        QuitTool()


if __name__ == "__main__":
    main()
