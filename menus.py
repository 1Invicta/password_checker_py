### [menus] ####

# --- Libs --- #
import os
from colorama import Fore, Style

# -- Modules - #
from checker import rate_password

# --- Info --- #
version = 0.5
last_update = "23/10/25"
repo_link = "https://github.com/1Invicta/password_checker"


# -- Visuals -- #
menu_options_top = "\n #===============#"
menu_options_bot = " #===============#"
header_box = " #--------------------------#"
exit_msg = f"\n [{Fore.RED}EXIT{Style.RESET_ALL}] - Closing..."


# --- Utils --- #
def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')

def cmd_title(title: str):
    os.system(f"title {title}")

def display_header(clear: bool):
    if clear:
        clr_scr()
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


# --- Menus --- #
def menu_main(clear: bool):
    display_header(clear)
    print(" Welcome to 'password_checker'!")
    print(" (This tool is still under development)\n")
    print(f" <===[{Style.BRIGHT}Main Menu{Style.RESET_ALL}]===>")
    print(" [1] - Check Your Password!")
    print(" [2] - Latest Updates")
    print(" [3] - Additional Information")
    print(f" [9] - {Fore.RED}Quit{Fore.RESET}")


def menu_update(clear: bool):
    display_header(clear)
    print(f" <===[{Style.BRIGHT}Latest Updates{Style.RESET_ALL}]==>")
    print(f" Current: [{Fore.LIGHTGREEN_EX}version-{version}{Style.RESET_ALL}]")
    print(f" [{Fore.YELLOW}!{Style.RESET_ALL}] NOTE: Refer to {Style.BRIGHT}'{repo_link}'{Style.RESET_ALL} for future updates.")

    print(f"\n * 28/09/25 - [{Fore.GREEN}ver-0.1{Style.RESET_ALL}]")
    print(f" [{Fore.GREEN}+{Fore.RESET}] Created main password checking framework system")
    print(f" [{Fore.GREEN}+{Fore.RESET}] Added menus and terminal user interface")
    print(f" [{Fore.YELLOW}/{Fore.RESET}] Fixed various menu and user interface bugs")
    print(f" [{Fore.RED}-{Fore.RESET}] Removed redundant code for optimization")

    print(f"\n * 06/10/25 - [{Fore.GREEN}ver-0.2{Style.RESET_ALL}]")
    print(f" [{Fore.YELLOW}/{Style.RESET_ALL}] Improved menus")
    print(f" [{Style.DIM}{Fore.YELLOW}/{Style.RESET_ALL}] Optimized code")

    print(f"\n * 07/10/25 - [{Fore.GREEN}ver-0.3{Style.RESET_ALL}]")
    print(f" [{Fore.YELLOW}/{Style.RESET_ALL}] Fixed bugs")
    print(f" [{Fore.YELLOW}/{Style.RESET_ALL}] Optimized menu system")

    print(f"\n * 09/10/25 - [{Fore.GREEN}ver-0.4{Style.RESET_ALL}]")
    print(f" [{Fore.YELLOW}/{Style.RESET_ALL}] Split scripts for modularization and readability")

    print(f"\n * {last_update} - [{Fore.LIGHTGREEN_EX}{version}{Style.RESET_ALL}]")
    print(f" [{Fore.GREEN}+{Style.RESET_ALL}] Uploaded tool to GitHub! (Check 'info' menu for the link)")
    print(f" [{Fore.YELLOW}/{Style.RESET_ALL}] Reorganized scripts for improved readability")
    print(f" [{Fore.RED}-{Style.RESET_ALL}] Removed reduntant code, variables and arguments")

    print(f"\n [9] - {Fore.RED}Back{Fore.RESET}")


def menu_info(clear: bool):
    display_header(clear)
    print(f" <===[{Style.BRIGHT}Additional Information{Style.RESET_ALL}]===>\n")
    print(" * Welcome to 'password_checker'!")
    print(" * This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.")
    print(f" * For future updates, refer to this repository: {Style.BRIGHT}'{repo_link}'{Style.RESET_ALL}.")
    print(f"\n [{Fore.YELLOW}!{Style.RESET_ALL}] NOTE: This tool is still under development.")

    print(f"\n [9] - {Fore.RED}Back{Fore.RESET}")

def password_checker(clear: bool):
    """Password checking loop"""
    display_header(clear)
    while True:
        display_header(True)
        print(f" <===[{Style.BRIGHT}Password Checker{Style.RESET_ALL}]===>\n")
        password = input(" <CMD/password_checker>: ")

        result = rate_password(password)
        print(f"\n This password is {result[1]}.")
        print(f" Rating: {result[2]}.")

        if result[0] == 1:
            print("\n Congratulations! Your password is safe.")
        elif result[0] == 0:
            print("\n Your password is alright, but you can make it stronger.")
        elif result[0] == -1:
            print("\n Your password is weak! Make it longer, add digits and special characters.")

        userinput = input("\n Try again? (y/n): ").lower()
        if userinput.startswith('y'):
            clr_scr()
            continue
        elif userinput.startswith('n'):
            clr_scr()
            print(f"\n [{Fore.RED}EXIT{Style.RESET_ALL}] - Closing...")
            break
        else:
            clr_scr()
            continue
