### [menus] ####

# --- Libs --- #
from colorama import Fore, Style


# --- Mods --- #
from checker import rate_password
from utils import *


# --- Info --- #
version = 0.7
last_update = "28/10/25"
repo_link = "https://github.com/1Invicta/password_checker_py"


#/  options   /#
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


# ===== Visuals ===== #
menu_options_top = "\n #===============#"
menu_options_bot = " #===============#"
exit_msg = DebugMsg("error", "Closing", True, False)

def build_box(length: int, topORbot: str):
    top = f"\n #{'='*length}#"
    bot = f" #{'='*length}#"
    
    if topORbot.lower().startswith('t'):
        print(top)
    else: print(bot)


def display_header(clear: bool):
    # needs improvement
    # pain to deal with. maybe ver-1.0?
    if clear: clr_scr()
    print(
        f" {header_box}\n"
        f"  | [{Fore.LIGHTMAGENTA_EX}password_checker_py{Style.RESET_ALL}]    |\n"
        f"  | [{Fore.LIGHTGREEN_EX}version-{version}{Style.RESET_ALL}] - {last_update} |\n"
        f"  |{Fore.LIGHTWHITE_EX}{Style.BRIGHT} Scripted by {Style.RESET_ALL}[{Fore.CYAN}{Style.BRIGHT}1Invicta{Style.RESET_ALL}]   |\n"
        f" {header_box}"
    )


def choose_menu():
    user_input = input("\n<CMD>: ")
    if user_input == '':
        return 0
    try:
        return int(user_input)
    except ValueError:
        return 0


def list_options(menu_id: int):
    """Displays available menus for the selected menu."""
    print(menu_options_top)
    
    options = (
        menu_options if menu_id == 0 else
        password_menu_options if menu_id == 1 else
        {9: "Back"}
    )

    for k, v in options.items():
        color = Fore.RED if k == 9 else Fore.WHITE
        print(f"  [{k}] - {PrintColor(v, color)}")
    
    print(menu_options_bot)


def list_password_diff_options():
    """Lists check settings."""
    settings = {
        # improve in ver-0.8
        1: f"{Fore.LIGHTGREEN_EX}Default {Fore.RESET}",
        2: f"{Fore.LIGHTBLUE_EX}Advanced{Fore.RESET}",
        3: f"{Fore.LIGHTMAGENTA_EX}Extreme {Fore.RESET}"
    }
    
    print(f"\n Current setting: [{write_current_setting(1)}]")

    build_box(menu_options_top, 16, "t")
    for k, v in settings.items():
        print(f"  [{k}] - [{v}]")
    #print(f"  [9] - [{Fore.RED}BACK{' '*(8-len('BACK'))}{Fore.RESET}]") // may reuse in the future
    print(f"  [9] - [{Fore.RED}BACK{Fore.RESET}]")
    build_box(menu_options_bot, 16, "b")


def display_menu_title(menu_id: int):
    """Displays the title for a given menu."""
    titles = {
        0: "/Home",
        1: "/password_checker_py",
        2: "/Latest-Updates",
        3: "/Info"
    }
    title = titles.get(menu_id, "/")
    print(f"\n<===[{title}]===>")


# ===== Menus ===== #
def menu_main(clear: bool):
    display_header(clear)
    display_menu_title(0)
    #print(" * Welcome to 'password_checker'!")
    #print(" * (This tool is still under development)")
    DebugMsg("info", "Welcome to 'password_checker_py'!", False, True)
    DebugMsg("warn", "NOTE: This tool is still under development", False, True)
    list_options(0)


def menu_update(clear: bool):
    display_header(clear)
    display_menu_title(2)
    
    display_current_version(version)

    # 28/09/2025
    display_latest_update("28/09/25", 0.1, False)
    #/// [NEW & AUTOMATED UPDATE(s) DISPLAY SYSTEM] ///
    DebugMsg("added", "Created main password checking framework system", False, True)
    DebugMsg("added", "Added menus and terminal user interface", False, True)
    DebugMsg("fix", "Fixed various menu and user interface bugs", False, True)
    DebugMsg("removed", "Removed redundant code for optimization", False, True)

    # 06/10/2025
    display_latest_update("06/10/25", 0.2, False)
    DebugMsg("fix", "Improved menus", False, True)
    DebugMsg("fix", "Optimized code", False, True)

    # 07/10/2025
    display_latest_update("07/10/25", 0.3, False)
    DebugMsg("fix", "Fixed bugs", False, True)
    DebugMsg("fix", "Optimized menu system", False, True)

    # 09/10/2025
    display_latest_update("09/10/25", 0.4, False)
    DebugMsg("fix", "Split scripts for modularization and readability", False, True)

    # 23/10/2025
    display_latest_update("23/10/25", 0.5, False)
    DebugMsg("added", "Uploaded tool to GitHub! (Check 'info' menu for the link)", False, True)
    DebugMsg("fix", "Reorganized scripts for improved readability", False, True)
    DebugMsg("removed", "Removed redundant code, variables and arguments", False, True)

    # 27/10/2025
    display_latest_update("27/10/25", 0.6, False)
    DebugMsg("added", "Added 'utils.py' script for helper functions", False, True)
    DebugMsg("added", "Added better comments for organization and readability", False, True)
    DebugMsg("fix", "Tweaked and improved menu system", False, True)
    DebugMsg("fix", "Automated up repetitive code and debugging", False, True)

    # LASTEST UPDATE
    display_latest_update(last_update, version, True)
    DebugMsg("added", "Added new password check features! ('Default', 'Advanced', 'Extreme')", False, True)
    DebugMsg("added", "Improved password check and rating system", False, True)
    DebugMsg("fix", "Fixed buggy 'utils.py' functions", False, True)
    DebugMsg("fix", "Fixed main menu bug: couldn't input '0' as valid menu", False, True)
    DebugMsg("fix", "Replaced redudant code with 'utils.py' helper functions", False, True)
    DebugMsg("removed", "Removed confusing comments", False, True)

    DebugMsg("warn", f"NOTE: Refer to '{repo_link}' for future updates.", True, True)
    list_options(2)


def menu_info(clear: bool):
    display_header(clear)
    display_menu_title(3)
    DebugMsg("info", "Welcome to 'password_checker'!", False, True)
    DebugMsg("info", f"This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.", False, True)
    DebugMsg("info", f"For future updates, refer to this GitHub repository: {repo_link} ", False, True)
    #print(" This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.")
    #print(f" For future updates, refer to this repository: '{repo_link}'.")
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


def password_options():
    list_password_diff_options()

    while True:
        choice = input("\n <CMD/password_checker_py>: ")
        
        if choice == "1":
            clr_scr()
            return 1
        
        elif choice == "2":
            clr_scr()
            return 2
        
        elif choice == "3":
            clr_scr()
            return 3
        
        elif choice == "9":
            clr_scr()
            return 9
        
        else:
            DebugMsg("warn", f"No available option given: Using default '[{write_current_setting(1)}]' settings!", True, True)
            input(" Type Enter to continue...")
            return 1


def write_current_setting(setting: int):
    if setting == 1:
        return PrintColor("Default", Fore.LIGHTGREEN_EX)
    elif setting == 2:
        return PrintColor("Advanced", Fore.LIGHTBLUE_EX)
    elif setting == 3:
        return PrintColor("Extreme", Fore.LIGHTMAGENTA_EX)


def password_checker(clear: bool):
    """Password checking loop."""
    while True:
        display_header(True)
        display_menu_title(1)
        
        check_setting = password_options()
        
        if check_setting != 9:
            display_header(True)
            display_menu_title(1)
            
            print(f"\n Current setting: [{write_current_setting(check_setting)}]")
            DebugMsg("tip", "Type your password!", False, True)

            password = input("\n <CMD/password_checker_py>: ")
            print(f"\n <===[{PrintColor("Checking password...", Fore.YELLOW, Style.BRIGHT)}]===>")
            
            rating, desc, score = rate_password(password, check_setting)

            print(f"\n <===[{PrintColor("RESULTS", Fore.GREEN, Style.BRIGHT)}]===>")
            print(f" => This password is {desc}.")
            print(f" => Rating: [{score}]")

            messages = {
                1: "Congratulations! Your password is safe.",
                0: "Your password is alright, but you can make it stronger.",
                -1: "Your password is weak! Make it longer, add digits and special characters."
            }
            print(f"\n {messages.get(rating, '')}")
            
            list_options(1)
            choice = retry_query()
            if choice == 9:
                clr_scr()
                continue
                
        if check_setting == 9:
            break
        continue
