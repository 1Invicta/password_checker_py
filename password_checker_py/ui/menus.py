# [ menus.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import logging
logger = logging.getLogger(__name__)
from colorama import Fore, Style


# [ Modules ] #
from ..core.generator import generate_password
from ..core.utils import DebugMsg, DebugInput, PrintColor, clr_scr, display_current_version
from ..data.changelog import repo_link
from .ui_logic import choose_menu, password_options, get_password_or_command, retry_query
from .visuals import LATEST_VERSION, LATEST_UPDATE_DATE, build_box, display_global_header, display_menu_title, display_mini_title, display_mini_sub_text, render_menu_header, list_options, write_current_check_mode, show_feedback, show_password_results, show_updates






# ======== Menus ======== #

def display_main_menu(clear: bool, wish_display_logo: bool = False):
    """Displays main menu content."""
    try:
        display_global_header(clear)
        display_menu_title(0, wish_logo=wish_display_logo)

        DebugMsg("info", "Welcome to 'password_checker_py'!", True, True)
        DebugMsg("warn", "NOTE: This tool is still under development", True, True)
        list_options(0, True, exclude_key=0, boxSize=23)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_main_menu' in 'menus.py'.", True, True)


def display_password_checker_menu(clear: bool, user_stats=None):
    """Displays password checker menu content."""
    check_setting = None
    newline = "\n"

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
                logger.debug("Password=%s, check_mode=%d", str(password), check_setting)

                show_password_results(str(password), check_setting, user_stats=user_stats)
                print(f"{newline}  <===[{PrintColor("FEEDBACK", Fore.YELLOW)}]===>")
                show_feedback()
                list_options(1, True)
                choice = retry_query()

                if choice == 0:
                    logger.info("Leaving checker menu...")
                    return
                elif choice == 1:
                    logger.info("Retrying password check...")
                    clr_scr()
                    continue
                elif choice == 9:
                    logger.info("Leaving retry submenu...")
                    clr_scr()
                    check_setting = None # go back = reset check mode
                    continue
            
            # reset to default
            clr_scr()
            check_setting = None

        except Exception:
            DebugMsg("error", "An unexpected error occurred: 'display_password_checker_menu' in 'menus.py'.", True, True)
            DebugInput("warn", "Press Enter to return to password checker.", False, True)
            continue


def display_password_generator_menu(clear: bool, user_stats: dict=None):
    """Displays password generator menu content."""
    check_setting = None
    newline = "\n"

    while True:
        try:
            render_menu_header(2)
            
            # choose check mode if not selected
            if check_setting is None:
                check_setting = password_options(useGenerator=True, submenu="Checker/Generator")
                if check_setting == 9:
                    clr_scr()
                    return
            
            # clear mode selection
            render_menu_header(2)
            write_current_check_mode(check_setting, True, True)
            DebugMsg("tip", "Press Enter to generate password!\n(Choosing a menu won't generate a password)", True, True)
            
            #list_password_check_modes(True, False)
            list_options(1, True, 1)
            cmd, generate = get_password_or_command(isGenerator=True) # type: ignore
            if cmd is None and generate is None:
                continue

            # command handling
            if cmd == 0:
                return
            elif cmd == 9:
                clr_scr()
                check_setting = None
                continue
            elif cmd is not None and cmd not in [0, 9]:
                DebugInput("warn", "Unavailable menu!", True, True)
                clr_scr()
                continue
            
            # generate handling
            if generate:
                render_menu_header(2)
                write_current_check_mode(check_setting, True, True)
                pass
            

            print(f"{newline}  <===[{PrintColor("GENERATOR", Fore.YELLOW)}]===>")
            generated_res = generate_password(check_setting, user_stats=user_stats)
            print(f"{newline} * Password: {generated_res}")
            list_options(1, True)
            choice = retry_query(True)

            if choice == 0:
                return
            elif choice == 1:
                clr_scr()
                continue
            elif choice == 9:
                clr_scr()
                check_setting = None
                continue

            clr_scr()
            check_setting = None

        except Exception:
            DebugMsg("error", "An unexpected error occurred: 'display_password_generator_menu' in 'menus.py'.", True, True)
            DebugInput("warn", "Press Enter to return to password generator.", False, True)
            continue


def display_changelog_menu(clear: bool):
    """Displays changelog menu content."""
    try:
        newline = "\n"
        display_global_header(clear)
        display_menu_title(3)
        
        # show version and last update date
        display_current_version(LATEST_VERSION)
        DebugMsg("info", f"Last updated on {LATEST_UPDATE_DATE}", False, True)

        # show recent updates
        show_updates(latest_only=True, count=2)
        
        # footer info
        print(f"{newline}  <===[{PrintColor("NOTE", Fore.YELLOW)}]===>")
        DebugMsg("warn", "Only the 2 most recent updates are shown here", False, True)
        DebugMsg("warn", f"Refer to '{repo_link}' for the full changelog", False, True)
        
        # options
        build_box("top", length=22)
        list_options(2, False, 0)
        build_box("bot", length=22)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_changelog_menu' in 'menus.py'.", True, True)
    

def display_help_menu(clear: bool):
    """Displays info menu content."""
    try:
        display_global_header(clear)
        display_menu_title(4)
        
        display_mini_title("INFO", Fore.YELLOW)
        # menu content
        display_mini_sub_text("Welome to 'password_checker'!")
        display_mini_sub_text("This tool is a prototype scripted in Python, but the real tool will be written in C, GO and/or Java.")
        display_mini_sub_text(f"For future updates, refer to this GitHub repository: '{repo_link}'.")

        display_mini_title("MENUS", Fore.LIGHTBLUE_EX, custom_index=1)
        display_mini_sub_text("[1] - Check password: type a password and get a score!")
        display_mini_sub_text("[2] - Generate password: select a mode to get a randomly generated password.")
        display_mini_sub_text("[3] - Changelog: see past updates and changes made to the tool.")
        display_mini_sub_text("[4] - Help: you're here!")
        display_mini_sub_text("[9] - Exits the tool.")
        DebugMsg("tip", "You can type Ctrl+C to safely quit the tool from any menu!", False, True)

        display_mini_title("MODES", Fore.LIGHTBLUE_EX, custom_index=2)
        display_mini_sub_text("[1] - Basic/Simple: the default and easiest mode to use.")
        display_mini_sub_text("[2] - Medium/Balanced: good for general-purpose safety.")
        display_mini_sub_text("[3] - Strong/Secure: the maximum safety!")

        display_mini_title("TERMINAL ARGUMENTS", Fore.LIGHTBLUE_EX, custom_index=3)
        DebugMsg("warn", "Terminal arguments can only be used outside this user interface\n \t You can use the following tags when executing this tool:", False, True)
        
        display_mini_sub_text("'-h/--help' - List argument tags, their descriptions and use-case examples", True)
        display_mini_sub_text("'-v/--version' - Display the tool's current version information", True)
        
        display_mini_sub_text("'-p/--password' - The password to check", True)
        display_mini_sub_text("'-cm/--check-mode' - Check mode of choice (1, 2 or 3)")
        display_mini_sub_text("Example: password_checker_py -p [PASSWORD (ex: 'test123')] -cm [CHECK-MODE (ex: 1)]")
        
        display_mini_sub_text("-g/--generate' - Generates a password", True)
        display_mini_sub_text("Example: password_checker_py -g -cm [CHECK-MODE (ex: 2)]")

        display_mini_sub_text("'-o/--output' - Saves results in a file (JSON)", True)
        display_mini_sub_text("Example: password_checker_py -g -cm [CHECK-MODE (ex: 3)] -o [OUTPUT file-name (ex: 'pizza')]")

        
        DebugMsg("warn", "NOTE: This tool is still under development", True, True)

        list_options(3, True)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_help_menu' in 'menus.py'.", True, True)






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

                display_menu_title(3, "Full Changelog")
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


