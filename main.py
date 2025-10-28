### [main] ###

## /dev NOTES/ ##
# (main.py) main loop => menu wrapper
# (menus.py) menus handler => each menu has its own loop
# (checker.py) password check system
# (utils.py) helper and debugging functions

# FUTURE (for ver-0.8+):
# - change function names!! they're super confusing
# - store last update notes and only display latest

# --- Mods --- #
from menus import menu_main, menu_info, menu_update, choose_menu, password_checker, clr_scr, exit_msg
from utils import DebugMsg, QuitTool

# --- Main --- #
def main():
    try:
        while True:
            menu_main(True)
            wish_menu = choose_menu()

            if wish_menu == 0:
                # stay
                continue

            elif wish_menu == 1:
                # password menu
                password_checker(True)

            elif wish_menu == 2:
                # updates menu
                while True:
                    # sub-menu loop
                    menu_update(True)
                    if choose_menu() == 9:
                        # exit sub-menu
                        break
                    else:
                        # stay in current menu
                        DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                        input("Type Enter to continue...")

            elif wish_menu == 3:
                # info menu
                while True:
                    # sub-menu loop
                    menu_info(True)
                    if choose_menu() == 9:
                        # exit sub-menu
                        break
                    else:
                        # stay in current menu
                        DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                        input("Type Enter to continue...")

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