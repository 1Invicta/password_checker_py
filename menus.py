#______ [menus] ______#


# =================== #
# ====== Setup ====== #
# =================== #

# --- Libs --- #
from colorama import Fore, Style

# --- Mods --- #
from utils import *
from checker import rate_password
from data.changelog import changelog, repo_link

# --- Info --- #
LATEST_VERSION = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]

# -- options - #
menu_options = {
    1: "Password!",
    2: "Changelog",
    3: "Help",
    9: "Quit"
}

password_menu_options = {
    0: "Home",
    1: "Retry",
    9: "Back"
}

changelog_menu_options = {
    0: "Home",
    1: "View all updates",
    9: "Back"
}


# =================== #
# ===== Visuals ===== #
# =================== #

menu_options_top = "\n #===============#"
menu_options_bot = " #===============#"

def build_box(topORbot: str, length: int=15):
    """Builds custom-sized options box. Defaults to a size of 15."""
    top = f"\n #{'='*length}#"
    bot = f" #{'='*length}#"
    
    if topORbot.lower().startswith('t'):
        print(top)
    else: print(bot)


def display_header(clear: bool):
    """Displays default header."""
    # needs improvement
    # pain to deal with. maybe ver-1.0?
    if clear: clr_scr()
    print(
        f" {header_box}\n"
        f"  | [{Fore.LIGHTMAGENTA_EX}password_checker_py{Style.RESET_ALL}]    |\n"
        f"  | [{Fore.LIGHTGREEN_EX}ver-{LATEST_VERSION}{Style.RESET_ALL}] - {LATEST_UPDATE_DATE} |\n"
        f"  |{Fore.LIGHTWHITE_EX}{Style.BRIGHT} Scripted by {Style.RESET_ALL}[{Fore.CYAN}{Style.BRIGHT}1Invicta{Style.RESET_ALL}]   |\n"
        f" {header_box}"
    )


def choose_menu(submenu: str=""):
    """Displays cmd-style input."""
    user_input = input(f"\n<CMD{f"/{submenu}" if submenu != "" else ""}>: ")
    if user_input == '':
        return 0
    try:
        return int(user_input)
    except ValueError:
        return 0


def list_options(menu_id: int, buildBox: bool, exclude_key: int=-1):
    """Displays available menus for the selected menu."""
    if buildBox: build_box('top')

    options = (
        menu_options if menu_id == 0 else
        password_menu_options if menu_id == 1 else
        changelog_menu_options if menu_id == 2 else
        {9: "Back"}
    )

    for k, v in options.items():
        if k == exclude_key: # skip said (key, value)
            continue

        color = Fore.RED if k == 9 else Fore.WHITE
        print(f"  [{k}] - {PrintColor(v, color)}")
    
    if buildBox: build_box('bot')


def list_password_diff_options():
    """Lists password check settings."""
    settings = {
        # get it fixed by ver-0.8
        1: f"{Fore.LIGHTGREEN_EX}Default {Fore.RESET}",
        2: f"{Fore.LIGHTBLUE_EX}Advanced{Fore.RESET}",
        3: f"{Fore.LIGHTMAGENTA_EX}Extreme {Fore.RESET}"
    }
    
    print(f"\n Current setting: [{write_current_setting(1)}]")

    build_box('t', 16)
    for k, v in settings.items():
        print(f"  [{k}] - [{v}]")
    #print(f"  [9] - [{Fore.RED}BACK{' '*(8-len('BACK'))}{Fore.RESET}]") // may reuse in the future
    print(f"  [9] - [{Fore.RED}BACK{Fore.RESET}]")
    build_box('b', 16)


def display_menu_title(menu_id: int, override: str=''):
    """Displays the title for a given menu."""
    titles = {
        0: "/Home",
        1: "/password_checker_py",
        2: "/Changelog",
        3: "/Help"
    }
    title = titles.get(menu_id, "/")
    print(f"\n<===[{title}]===>" if override=='' else f"\n<===[{str(override)}]===>")



# =================== #
# === Extractions === #
# =================== #

def retry_query():
    while True:
        user_input = input("\n<CMD/password_checker_py>: ")

        if user_input == "0":
            return 0
        
        elif user_input == "1":
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
        choice = choose_menu("password_checker_py")
           
        if choice == 1:
            clr_scr()
            return 1

        elif choice == 2:
            clr_scr()
            return 2
        
        elif choice == 3:
            clr_scr()
            return 3
        
        elif choice == 9:
            clr_scr()
            return 9
        
        else:
            DebugMsg("warn", f"No available option given: Using '[{write_current_setting(1)}]' settings!", True, True)
            DebugInput("System", "Type Enter to continue...", False, True)
            return 1


def write_current_setting(setting: int):
    if setting == 1:
        return PrintColor("Default", Fore.LIGHTGREEN_EX)
    elif setting == 2:
        return PrintColor("Advanced", Fore.LIGHTBLUE_EX)
    elif setting == 3:
        return PrintColor("Extreme", Fore.LIGHTMAGENTA_EX)


def show_updates(latest_only=True, count=3):
    # reverse update list order
    ordered = list(reversed(changelog))
    updates_to_show = ordered[:count] if latest_only else ordered

    for update in updates_to_show:
        display_latest_update(update["date"], update["version"], True if update["version"] == LATEST_VERSION else False)
        for change_type, msg in update["changes"]:
            DebugMsg(change_type, msg, False, True)



# =================== #
# ====== Menus ====== #
# =================== #

def display_main_menu(clear: bool):
    """Displays main menu content."""
    display_header(clear)
    display_menu_title(0)
    #print(" * Welcome to 'password_checker'!")
    #print(" * (This tool is still under development)")
    DebugMsg("info", "Welcome to 'password_checker_py'!", True, True)
    DebugMsg("warn", "NOTE: This tool is still under development", True, True)
    list_options(0, True, exclude_key=0)


def display_changelog_menu(clear: bool):
    """Displays changelog menu content."""
    display_header(clear)
    display_menu_title(2)
    
    # show version and last update date
    display_current_version(LATEST_VERSION)
    DebugMsg("info", f"Latest update on {LATEST_UPDATE_DATE}", False, True)

    # show recent updates
    show_updates(latest_only=True, count=3)
    
    # footer info
    DebugMsg("warn", "NOTE: Only the 3 most recent updates are shown here", True, True)
    DebugMsg("warn", f"Refer to '{repo_link}' for the full changelog", True, True)
    
    # options
    build_box('top', length=22)
    list_options(2, False, 0)
    build_box('bot', length=22)
    

def display_help_menu(clear: bool):
    """Displays info menu content."""
    display_header(clear)
    display_menu_title(3)
    DebugMsg("info", "Welcome to 'password_checker'!", True, True)
    DebugMsg("info", f"This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.", False, True)
    DebugMsg("info", f"For future updates, refer to this GitHub repository: {repo_link} ", False, True)
    #print(" This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.")
    #print(f" For future updates, refer to this repository: '{repo_link}'.")
    DebugMsg("warn", "NOTE: This tool is still under development", True, True)

    list_options(3, True)


def display_password_checker_menu(clear: bool):
    """Password checking loop."""
    # store user's chosen settting
    check_setting = None

    while True:
        try:
            display_header(True)
            display_menu_title(1)
            
            # check if setting not yet chosen
            if check_setting is None:
                check_setting = password_options()
                if check_setting == 9:
                    clr_scr()
                    return
            
            display_header(True)
            display_menu_title(1)

            print(f"\n Current setting: [{write_current_setting(check_setting)}]")
            DebugMsg("tip", "Type your password!", True, True)
            list_options(1, True, 1)

            userinput = input("\n<CMD/password_checker_py>: ")

            try:
                converted_input = int(userinput)
            
                if converted_input == 0:
                    display_main_menu(True)
                    break
                elif converted_input == 9:
                    clr_scr()
                    check_setting = None
                    continue
                
            except ValueError:
                password = userinput
            
            if not userinput.strip():
                DebugMsg("warn", "Empty input. Please enter a password.", False, True)
                input("Press Enter to retry...")
                continue
            
            # redraw for clarity
            display_header(True)
            display_menu_title(1)

            print(f"\n  <===[{PrintColor("Checking password", Fore.YELLOW, Style.BRIGHT)}]===>")
            
            rating, desc, score = rate_password(password, check_setting)
            
            print(f"\n  <===[{PrintColor("RESULTS", Fore.GREEN, Style.BRIGHT)}]===>")
            print(f"   => This password is {desc}.")
            print(f"   => Rating: [{score}]")

            messages = {
                1: "Congratulations! Your password is safe.",
                0: "Your password is alright, but you can make it stronger.",
                -1: "Your password is weak! Make it longer, add digits and special characters."
            }
            print(f"\n {messages.get(rating, '')}")
            
            list_options(1, True)
            choice = retry_query()

            if choice == 0:
                display_main_menu(True)
                break
            elif choice == 1:
                clr_scr()
                continue
            elif choice == 9:
                clr_scr()
                check_setting = None
                continue
            
            # fallback: reset to default case
            clr_scr()
            check_setting = None

        except Exception:
            DebugMsg("error", "An unexpected error occured. Returning to password checker.", False, True)
            continue

    clr_scr()
        



# =================== #
# ==== Sub-Menus ==== #
# =================== #

def display_changelog_submenu():
    """Submenu for changelog menu. Allows viewing recent or all updates. Has its own loop."""
    while True:
        # start submenu loop
        display_changelog_menu(clear=True)
        
        choice = choose_menu("Changelog")
        
        if choice == 1:
            # display full changelog
            display_header(True)

            display_menu_title(2, "Full Changelog")
            show_updates(latest_only=False)

            DebugMsg("warn", "End of changelog.", True, True)
            DebugInput("tip", "Press Enter to return to changelog menu...", True, True)
        
        elif choice == 9:
            # exit sub-menu
            clr_scr()
            break
        else:
            # stay in current menu
            DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
            input("Type Enter to continue...")


def display_help_submenu():
    """Submenu for info. Has its own loop."""
    while True:
        # start submenu loop
        display_help_menu(True)
        
        choice = choose_menu("Help")
     
        if choice == 9:
            # exit sub-menu
            clr_scr()
            break
        else:
            # stay in current menu
            DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
            input("Type Enter to continue...")


