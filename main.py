#____ [main] ____#


# ========================= NOTES ========================== #

# (main.py) main loop => wrapper for everything
# (menus.py) menus handler => each menu has its own submenu
# (changelog.py) stores all past updates
# (checks.py) password check system
# (utils.py) helper and debugging functions

# ========================================================== #



# FUTURE (ver-0.3.4):
# [/] - implement entropy-based checks

# --- Mods --- #
from menus import *
from utils import DebugMsg, QuitTool, exit_msg, cmd_title

# --- Main --- #
def main():
    """Main 'password_checker_py' program."""
    try:
        while True:
            cmd_title("password_checker_py - Home")
            # main loop
            display_main_menu(True)
            wish_menu = choose_menu()

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
                DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                input("Type Enter to continue...")
                continue
    except:
        QuitTool()


if __name__ == "__main__":
    main()
