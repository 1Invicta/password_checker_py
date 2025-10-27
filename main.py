### [main] ###

## /dev NOTES/ ##
# (1) each menu has its own loop
# (2) utils.py is mainly used for debugging

# --- Mods --- #
from menus import menu_main, menu_info, menu_update, choose_menu, password_checker, clr_scr, exit_msg
from utils import DebugMsg

# --- Main --- #
def main():
    while True:
        menu_main(True)
        wish_menu = choose_menu()

        if wish_menu == 1:
            # password menu
            password_checker(True)

        elif wish_menu == 2:
            # updates menu
            while True:
                menu_update(True)
                if choose_menu() == 9:
                    break
                else:
                    # stay in current menu
                    DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                    input("Type Enter to continue...")

        elif wish_menu == 3:
            while True:
                menu_info(True)
                if choose_menu() == 9:
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


if __name__ == "__main__":
    main()