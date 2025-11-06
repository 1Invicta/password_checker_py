# [ menus.py ] #


# ======== Setup ======== #

# [ Libraries ] #
from colorama import Fore, Style


# [ Modules ] #
import core.checks as checks
from ui.visuals import header_box
from data.changelog import changelog, repo_link
from core.utils import DebugMsg, DebugInput, PrintColor, clr_scr, display_current_version, display_latest_update


# [ Information ] #
LATEST_VERSION = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]


# [ options ] #
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


def build_box(topORbot: str, length: int=15, wish_print: bool=True):
    """Builds custom-sized options box. Defaults to a size of 15."""
    try:
        top = f"\n #{'='*length}#"
        bot = f" #{'='*length}#"
        
        if topORbot.lower().startswith('t'):
            if wish_print:
                print(top)
            return top
        else:
            if wish_print:
                print(bot)
            return bot
    
    except Exception:
        DebugMsg("error", f"An unexpected error occurred: 'build_box' in 'menus.py'.", True, True)


def display_global_header(clear: bool):
    """Displays default header."""
    # needs improvement
    # pain to deal with. maybe ver-1.0?
    try:
        if clear: clr_scr()
        print(
            f" {build_box(header_box, length=26, wish_print=False)}\n"
            f"  | [{Fore.LIGHTMAGENTA_EX}password_checker_py{Style.RESET_ALL}]    |\n"
            f"  | [{Fore.LIGHTGREEN_EX}ver-{LATEST_VERSION}{Style.RESET_ALL}] - {LATEST_UPDATE_DATE} |\n"
            f"  |{Fore.LIGHTWHITE_EX}{Style.BRIGHT} Scripted by {Style.RESET_ALL}[{Fore.CYAN}{Style.BRIGHT}1Invicta{Style.RESET_ALL}]   |\n"
            f" {build_box(header_box, length=26, wish_print=False)}"
        )

    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_global_header' in 'menus.py'.", True, True)


def display_menu_title(menu_id: int, override: str=''):
    """Displays the title for a given menu."""
    try:
        titles = {
            0: "/Home",
            1: "/password_checker_py",
            2: "/Changelog",
            3: "/Help"
        }
        title = titles.get(menu_id, "/")
        print(f"\n<===[{title}]===>" if override=='' else f"\n<===[{str(override)}]===>")
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_menu_title' in 'menus.py'.", True, True)


def render_menu_header(menu_id: int):
    try:
        display_global_header(True)
        display_menu_title(menu_id)

    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'render_menu_header' in 'menus.py'.", True, True)


def choose_menu(easter_egg: bool=False, submenu: str=""):
    """Displays cmd-style input."""
    try:
        #user_input = input(f"\n<CMD{f"/{submenu}" if submenu != "" else ""}>: ")
        user_input = input(f"\n<CMD{'/' + submenu if submenu != '' else ''}>: ")
        if user_input == '' or not user_input:
            return 0
        elif  easter_egg and user_input in ("1Invicta", "Invicta"):
            DebugInput("tip", "That's me! ", True, True)
            return 0
        try:
            return int(user_input)
        except ValueError:
            return 0

    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'choose_menu' in 'menus.py'.", True, True)
        return 0


def list_options(menu_id: int, buildBox: bool, exclude_key: int=-1):
    """Displays available menus for the selected menu."""
    try:
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
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'list_options' in 'menus.py'.", True, True)


def list_password_check_modes():
    """Lists password check settings."""
    try:
        settings = {
            # get it fixed
            1: f"{Fore.LIGHTGREEN_EX}Default {Fore.RESET}",
            2: f"{Fore.LIGHTBLUE_EX}Advanced{Fore.RESET}",
            3: f"{Fore.LIGHTMAGENTA_EX}Extreme {Fore.RESET}"
        }
        
        print(f"\n Current setting: [{write_current_check_mode(1)}]")

        build_box('t', 16)
        for k, v in settings.items():
            print(f"  [{k}] - [{v}]")
        #print(f"  [9] - [{Fore.RED}BACK{' '*(8-len('BACK'))}{Fore.RESET}]") // may reuse in the future
        print(f"  [9] - [{Fore.RED}BACK{Fore.RESET}]")
        build_box('b', 16)
     
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'list_password_check_modes' in 'menus.py'.", True, True)







# ======== Extractions ======== #

# for password menu
def write_current_check_mode(setting: int, wish_print: bool=False):
    """Returns currently selected check mode for password checking."""
    try:
        if setting == 1:
            if wish_print: print(f"\n Current mode: [{PrintColor("Default", Fore.LIGHTGREEN_EX)}]")
            return f"\n Current mode: {PrintColor("Default", Fore.LIGHTGREEN_EX)}"
        elif setting == 2:
            if wish_print: print(f"\n Current mode: [{PrintColor("Advanced", Fore.LIGHTBLUE_EX)}]")
            return f"\n Current mode: {PrintColor("Advanced", Fore.LIGHTBLUE_EX)}"
        elif setting == 3:
            if wish_print: print(f"\n Current mode: [{PrintColor("Extreme", Fore.LIGHTMAGENTA_EX)}]")
            return f"\n Current mode: {PrintColor("Extreme", Fore.LIGHTMAGENTA_EX)}"
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'write_current_setting' in 'menus.py'.", True, True)


def password_options():
    """Handles input choice for password check mode."""
    try:
        list_password_check_modes()

        while True:
            choice = choose_menu(easter_egg=False, submenu="password_checker_py")
            
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
                DebugMsg("warn", f"No available option given: Using [{write_current_check_mode(1)}] settings!", True, True)
                DebugInput("System", "Type Enter to continue...", False, True)
                return 1
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'password_options' in 'menus.py'.", True, True)


def get_password_or_command():
    """Returns a tuple (command, password) from user input."""
    try:
        userinput = input("\n<CMD/password_checker_py>: ").strip()
        if not userinput:
            DebugMsg("warn", "Empty input. Please enter a password.", False, True)
            DebugInput("tip", "Press Enter to retry...", False, True)
            return None, None
        
        # userinput is either command or password
        try:
            return int(userinput), None
        
        except ValueError:
            return None, userinput
    
    except Exception:
        DebugMsg("error", "An unexpected error occured: 'get_password_or_command' in 'menus.py'.", True, True)


def show_feedback():
    """Display feedback to improve password."""

    if checks.cl: print("    * Make your password longer.")
    if checks.cc: print("    * Use upper and lowercase characters.")
    if checks.cd: print("    * Add digits.")
    if checks.cs: print("    * Use special characters.")
    if checks.cp: print("    * Avoid patterns in your password.")
    if checks.cw: print("    * Find a less common password.")
    if checks.ce: print("    * Make your password less obvious.")


def show_password_results(password: str, check_setting: int):
    """Displays password rating and advice based on user iinput."""
    try:
        render_menu_header(1)
        write_current_check_mode(check_setting, True)
        display_menu_title(1, override=PrintColor("Checking password", Fore.YELLOW, Style.BRIGHT))

        rating, desc, score = checks.rate_password(password, check_setting)

        print(f"\n  <===[{PrintColor("RESULTS", Fore.GREEN, Style.BRIGHT)}]===>")
        print(f"   => This password is {desc}.")
        print(f"   => Rating [{score}]")

        messages = {
            1: "Congratulations! Your password is safe.",
            0: "Your password is alright, but you can make it stronger.",
            -1: "Your password is weak! Make it stronger, add digits and special characters."
        }
        print(f"\n {messages.get(rating, '')}")
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'show_password_results' in 'menus.py'.", True, True)


def retry_query():
    """Queries user to retry for a password check."""
    try:
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
                DebugInput("tip", "Type Enter to continue...", False, True)
                render_menu_header(1)
                write_current_check_mode(1, True)
                list_options(1, True)
                continue

    except Exception:
        DebugMsg("error", "An unexpected error occured: 'retry_query' in 'menus.py'.", True, True)
        return 0


# for changelog menu
def show_updates(latest_only: bool=True, count: int=3):
    """Display 3 latest updates from changelog, optionally as many as wished."""
    try:
        # reverse update list order
        ordered = list(reversed(changelog))
        updates_to_show = ordered[:count] if latest_only else ordered

        for update in updates_to_show:
            display_latest_update(update["date"], update["version"], True if update["version"] == LATEST_VERSION else False)
            for change_type, msg in update["changes"]:
                DebugMsg(change_type, msg, False, True)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'show_updates' in 'menus.py'.", True, True)






# ======== Menus ======== #

def display_main_menu(clear: bool):
    """Displays main menu content."""
    try:
        display_global_header(clear)
        display_menu_title(0)

        DebugMsg("info", "Welcome to 'password_checker_py'!", True, True)
        DebugMsg("warn", "NOTE: This tool is still under development", True, True)
        list_options(0, True, exclude_key=0)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_main_menu' in 'menus.py'.", True, True)


def display_changelog_menu(clear: bool):
    """Displays changelog menu content."""
    try:
        display_global_header(clear)
        display_menu_title(2)
        
        # show version and last update date
        display_current_version(LATEST_VERSION)
        DebugMsg("info", f"Latest update on {LATEST_UPDATE_DATE}", False, True)

        # show recent updates
        show_updates(latest_only=True, count=2)
        
        # footer info
        print(f"\n  <===[{PrintColor("NOTE", Fore.YELLOW)}]===>")
        DebugMsg("warn", "Only the 2 most recent updates are shown here", False, True)
        DebugMsg("warn", f"Refer to '{repo_link}' for the full changelog", False, True)
        
        # options
        build_box('top', length=22)
        list_options(2, False, 0)
        build_box('bot', length=22)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_changelog_menu' in 'menus.py'.", True, True)
    

def display_help_menu(clear: bool):
    """Displays info menu content."""
    try:
        display_global_header(clear)
        display_menu_title(3)
        
        # menu content
        DebugMsg("info", "Welcome to 'password_checker'!", True, True)
        DebugMsg("info", f"This tool is a prototype scripted in Python, but the real tool will be written in C and/or C#.", False, True)
        DebugMsg("info", f"For future updates, refer to this GitHub repository: {repo_link} ", False, True)

        DebugMsg("warn", "NOTE: This tool is still under development", True, True)

        list_options(3, True)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_help_menu' in 'menus.py'.", True, True)


def display_password_checker_menu(clear: bool):
    """Displays password checker menu content."""
    check_setting = None

    while True:
        try:
            render_menu_header(1)

            # choose check mode if not selected
            if check_setting is None:
                check_setting = password_options()
                if check_setting == 9:
                    clr_scr()
                    return
            
            # clear mode selection
            render_menu_header(1)
            write_current_check_mode(check_setting, True)
            DebugMsg("tip", "Type your password!", True, True)
            list_options(1, True, 1)

            cmd, password = get_password_or_command() # type: ignore
            if cmd is None and password is None:
                continue

            # command handling
            if cmd == 0:
                return # main menu
            elif cmd == 9:
                clr_scr()
                check_setting = None # reset check mode + go back
                continue

            # password checking and result display
            if password:
                show_password_results(str(password), check_setting)
                print(f"\n  <===[{PrintColor("FEEDBACK", Fore.YELLOW)}]===>")
                show_feedback()
                list_options(1, True)
                choice = retry_query()

                if choice == 0:
                    return
                elif choice == 1:
                    clr_scr()
                    continue
                elif choice == 9:
                    clr_scr()
                    check_setting = None # go back = reset check mode
                    continue
            
            # reset to default
            clr_scr()
            check_setting = None

        except Exception:
            DebugMsg("error", "An unexpected error occurred: 'display_password_checker_menu' in 'menus.py'.", True, True)
            DebugInput("warn", "Returning to password checker.", False, True)
            continue






# ======== Sub-Menus ======== #

def display_changelog_submenu():
    """Submenu for changelog menu. Allows viewing recent or all updates. Has its own loop."""
    while True:
        try:
            # start submenu loop
            display_changelog_menu(clear=True)
            
            choice = choose_menu(easter_egg=False, submenu="Changelog")
            
            if choice == 1:
                # display full changelog
                display_global_header(True)

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
                DebugInput("tip", "Type Enter to continue...", False, True)
        
        except Exception:
            DebugMsg("error", "An unexpected error occurred: 'display_changelog_submenu' in 'menus.py'.", True, True)


def display_help_submenu():
    """Submenu for info. Has its own loop."""
    while True:
        try:
            # start submenu loop
            display_help_menu(True)
            
            choice = choose_menu(easter_egg=False, submenu="Help")
        
            if choice == 9:
                # exit sub-menu
                clr_scr()
                break
            else:
                # stay in current menu
                DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                DebugInput("tip", "Type Enter to continue...", False, True)
        
        except Exception:
            DebugMsg("error", "An unexpected error occurred: 'display_help_submenu' in 'menus.py'.", True, True)


