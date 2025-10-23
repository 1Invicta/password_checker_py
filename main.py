### [main] ###

# --- Mods --- #
from menus import menu_main, menu_info, menu_update, choose_menu, password_checker, clr_scr, exit_msg

# --- Main --- #
def main():
    while True:
        menu_main(True)
        wish_menu = choose_menu()

        if wish_menu == 1:
            password_checker(True)

        elif wish_menu == 2:
            menu_update(True)
            if choose_menu() == 9:
                continue

        elif wish_menu == 3:
            menu_info(True)
            if choose_menu() == 9:
                continue

        elif wish_menu == 9:
            clr_scr()
            print(exit_msg)
            break
        else:
            continue

if __name__ == "__main__":
    main()