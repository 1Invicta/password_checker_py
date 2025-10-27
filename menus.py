### [menus] ####

# --- Libs --- #
from colorama import Fore, Style

# -- Modules - #
from checker import rate_password
from utils import DebugMsg, PrintColor, clr_scr

# --- Info --- #
version = 0.6
last_update = "27/10/25"
repo_link = "https://github.com/1Invicta/password_checker_py"

#_home_options_#
menu_options = {
    0: "Home",
    1: "Password!",
    2: "Updates",
    3: "Info",
    9: "Quit"
}

password_menu_options = {
    1: "Retry",
    9: "Back"
}

# -- Visuals -- #
menu_options_top = "\n #===============#"
menu_options_bot = " #===============#"
header_box = " #--------------------------#"
exit_msg = DebugMsg("error", "Closing", True, False)


# --- Helpr --- #
def display_header(clear: bool):
    if clear: clr_scr()
    print(
        f" {header_box}\n"
        f"  | [{Fore.LIGHTMAGENTA_EX}password_checker{Style.RESET_ALL}]       |\n"
        f"  | [{Fore.GREEN}version-{version}{Style.RESET_ALL}] - {last_update} |\n"
        f"  |{Fore.LIGHTBLACK_EX}{Style.BRIGHT} Scripted by {Style.RESET_ALL}[{Fore.CYAN}{Style.BRIGHT}1Invicta{Style.RESET_ALL}]   |\n"
        f" {header_box}"
    )

def choose_menu():
    user_input = input("\n</CMD>: ")
    if user_input == '':
        return 0
    try:
        return int(user_input)
    except ValueError:
        return 0


def list_options(wish_menu: int):
    print(menu_options_top)
    
    if wish_menu == 0:
        for k, v in menu_options.items():
            if k != 9:
                print(f"  [{k}] - {v}")
        print(f"  [9] - {PrintColor("Quit", Fore.RED)}")
    
    elif wish_menu == 1:
        for k, v in password_menu_options.items():
            if k != 9:
                print(f"  [{k}] - {v}")
        print(f"  [9] - {PrintColor("Back", Fore.RED)}")
    
    else:
        print(f"  [9] - {PrintColor("Back", Fore.RED)}")
    print(menu_options_bot)


def display_menu_title(menu: int):
    if menu == 0:
        print("\n<===[/Home]===>")
    
    elif menu == 1:
        print("\n<===[/password_checker_py]===>")
    
    elif menu == 2:
        print("\n<===[/Latest-Updates]===>")
    
    elif menu == 3:
        print("\n<===[/Info]===>")
    
    else:
        print("\n<===[/]===>")


# --- Menus --- #
def menu_main(clear: bool):
    display_header(clear)
    display_menu_title(0)
    print(" * Welcome to 'password_checker'!")
    print(" * (This tool is still under development)")
    list_options(0)


def menu_update(clear: bool):
    display_header(clear)
    display_menu_title(2)
    
    # display current version
    print(f" Current: [{PrintColor(f"version-{version}", Fore.GREEN, Style.BRIGHT)}]")
    DebugMsg("warn", f"NOTE: Refer to '{repo_link}' for future updates.", False, True)

    # 28/09/2025
    print(f"\n * 28/09/25 - [{Fore.GREEN}ver-0.1{Style.RESET_ALL}]")
    #/// [OLD & MANUAL UPDATE(s) DISPLAY SYSTEM] ///
    #print(f" [{Fore.GREEN}+{Fore.RESET}] Created main password checking framework system")
    #print(f" [{Fore.GREEN}+{Fore.RESET}] Added menus and terminal user interface")
    #print(f" [{Fore.YELLOW}/{Fore.RESET}] Fixed various menu and user interface bugs")
    #print(f" [{Fore.RED}-{Fore.RESET}] Removed redundant code for optimization")

    #/// [NEW & AUTOMATED UPDATE(s) DISPLAY SYSTEM] ///
    DebugMsg("added", "Created main password checking framework system", False, True)
    DebugMsg("added", "Added menus and terminal user interface", False, True)
    DebugMsg("fix", "Fixed various menu and user interface bugs", False, True)
    DebugMsg("removed", "Removed redundant code for optimization", False, True)

    # 06/10/2025
    print(f"\n * 06/10/25 - [{Fore.GREEN}ver-0.2{Style.RESET_ALL}]")
    DebugMsg("fix", "Improved menus", False, True)
    DebugMsg("fix", "Optimized code", False, True)

    # 07/10/2025
    print(f"\n * 07/10/25 - [{Fore.GREEN}ver-0.3{Style.RESET_ALL}]")
    DebugMsg("fix", "Fixed bugs", False, True)
    DebugMsg("fix", "Optimized menu system", False, True)

    # 09/10/2025
    print(f"\n * 09/10/25 - [{Fore.GREEN}ver-0.4{Style.RESET_ALL}]")
    DebugMsg("fix", "Split scripts for modularization and readability", False, True)

    # 23/10/2025
    print(f"\n * 23/10/25 - [{Fore.GREEN}ver-0.5{Style.RESET_ALL}]")
    DebugMsg("added", "Uploaded tool to GitHub! (Check 'info' menu for the link)", False, True)
    DebugMsg("fix", "Reorganized scripts for improved readability", False, True)
    DebugMsg("removed", "Removed redundant code, variables and arguments", False, True)

    # LAST UPDATE
    print(f"\n * {last_update} - [{Fore.LIGHTGREEN_EX}ver-{version}{Style.RESET_ALL}]")
    DebugMsg("added", "Added 'utils.py' script for helper functions", False, True)
    DebugMsg("added", "Added better comments for organization and readability", False, True)
    DebugMsg("fix", "Tweaked and improved menu system", False, True)
    DebugMsg("fix", "Automated up repetitive code and debugging", False, True)

    list_options(2)


def menu_info(clear: bool):
    display_header(clear)
    display_menu_title(3)
    print(" * Welcome to 'password_checker'!")
    print(" * This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.")
    print(f" * For future updates, refer to this repository: {Style.BRIGHT}'{repo_link}'{Style.RESET_ALL}.")
    DebugMsg("warn", "NOTE: This tool is still under development", True, True)

    list_options(3)


def retry_query():
    while True:
        user_input = input("\n<CMD/password_checker_py>: ")

        if user_input == "1":
            clr_scr()
            return 1
        
        elif user_input == "9":
            clr_scr()
            DebugMsg("error", "Closing", True, True)
            return 9
        
        else:
            DebugMsg("error", "Invalid input: Please type a listed option!", False, True)
            input(" Type Enter to continue...")


def password_checker(clear: bool):
    """Password checking loop"""
    display_header(clear)
    while True:
        display_header(True)
        display_menu_title(1)
        password = input("\n <CMD/password_checker_py>: ")

        result = rate_password(password)
        print(f"\n This password is {result[1]}.")
        print(f" Rating: {result[2]}.")

        if result[0] == 1:
            print("\n Congratulations! Your password is safe.")
        elif result[0] == 0:
            print("\n Your password is alright, but you can make it stronger.")
        elif result[0] == -1:
            print("\n Your password is weak! Make it longer, add digits and special characters.")

        list_options(1)
        choice = retry_query()

        if choice == 1:
            clr_scr()
            continue
        elif choice == 9:
            clr_scr()
            break
