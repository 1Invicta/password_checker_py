# [ menus.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import   logging
import      time

logger = logging.getLogger(__name__)

from colorama       import Fore
from inputimeout    import TimeoutOccurred


# [ Modules ] #
from ..core.cli         import display_user_stats, display_version_info
from ..core.checks      import rate_password
from ..core.generator   import generate_password
from ..core.utils       import DebugMsg, DebugInput, PrintColor, clr_scr, display_current_version
from ..data.changelog   import repo_link
from ..data.data        import DATE_TODAY
from ..data.save        import save_result
from .ui_logic          import choose_menu, password_options, get_password_or_command, retry_query
from .visuals import (
    LATEST_VERSION, LATEST_UPDATE_DATE, build_box, display_global_header, 
    display_menu_title, display_mini_title, display_mini_sub_text, render_menu_header, 
    list_options, write_current_check_mode, show_feedback, show_password_results, show_updates
)






# ======== Menus ======== #

def display_main_menu( clear: bool, wish_display_logo: bool = False, user_stats: dict=None ):
    """Displays main menu content."""
    
    logger.info("'display_main_menu' executed.")
    
    start_time = time.perf_counter()

    try:
        display_global_header(clear)
        display_menu_title(0, wish_logo=wish_display_logo)

        DebugMsg("info", "Welcome to 'password_checker_py'!", True, True)
        DebugMsg("warn", "NOTE: This tool is still under development", True, True)
        list_options(0, True, exclude_key=0, boxSize=23)
    
    except Exception:
        logger.exception("Exception found: ")
        DebugMsg("error", "An unexpected error occurred: 'display_main_menu' in 'menus.py'.", True, True)
    
    finally:
        if user_stats is not None:
            user_stats["total_sessions_seconds"] += time.perf_counter() - start_time
            logger.info("Successfully updated user stats")
        


def display_password_checker_menu( user_stats: dict=None ):
    """Displays password checker menu content."""
    
    logger.info("'display_password_checker_menu' executed.")

    check_setting = None
    newline = "\n"

    while True:
        loop_start = time.perf_counter()
        
        try:
            render_menu_header(1)

            # choose check mode if not selected
            if check_setting is None:

                check_setting = password_options()
                logger.info("Checkmode chosen = %d", check_setting)
                
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
                
                return             # main menu
            
            elif cmd == 9:
                clr_scr()
                check_setting = None # reset check mode + go back
                continue

            # password checking and result display
            if password:
                logger.debug("Password=%s, check_mode=%d", str(password), check_setting)

                show_password_results(str(password), check_setting, user_stats=user_stats)
                
                colored_feedback_title_msg = PrintColor("FEEDBACK", Fore.YELLOW)
                print(f"{newline}  <===[{colored_feedback_title_msg}]===>")
                
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
                    
                    # reset check mode to allow user set their own
                    check_setting = None
                    continue
            
            # reset to default
            clr_scr()
            check_setting = None

        except Exception:
            logger.exception("Exception found: ")
            DebugMsg("error", "An unexpected error occurred: 'display_password_checker_menu' in 'menus.py'.", True, True)
            DebugInput("warn", "Press Enter to return to password checker.", False, True)
            continue

        finally:
            if user_stats is not None:
                user_stats["total_sessions_seconds"] += time.perf_counter() - loop_start
                logger.info("Successfully updated user stats")


def display_password_generator_menu( user_stats: dict=None ):
    """Displays password generator menu content."""

    logger.info("'display_password_generator' executed.")
    
    check_setting = None
    newline = "\n"

    while True:
        loop_start = time.perf_counter()
        try:
            render_menu_header(2)
            
            # choose check mode if not selected
            if check_setting is None:
                check_setting = password_options(useGenerator=True, submenu="Checker/Generator")
                logger.info("Checkmode chosen = %d", check_setting)

                if check_setting == 9:
                    logger.info("Returning to previous menu.")
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
                logger.info("Leaving to home menu...")
                
                return
            
            elif cmd == 9:
                logger.info("Leaving generator submenu")
                clr_scr()
                check_setting = None
                continue
            
            elif cmd is not None and cmd not in [0, 9]:
                logger.info("Invalid menu selected: not in [0, 9]")
                DebugInput("warn", "Unavailable menu!", True, True)
                clr_scr()
                continue
            
            # generate handling
            if generate:
                render_menu_header(2)
                write_current_check_mode(check_setting, True, True)
                DebugMsg("warn", "Enter number of passwords to generate (defaults to 1): ", True, True)
                
                try:
                    pre_amount = choose_menu(submenu="Checker/Generator/Amount")
                    
                    if pre_amount is not None:
                        post_amount = pre_amount
                    
                    else:
                        post_amount = 0
                
                except ValueError:
                    DebugMsg("warn", "Invalid input. Using default value.", False, True)
                    post_amount = 0
                
                except Exception:
                    DebugMsg("error", "An unexpected error occured. Using default value.", False, True)
                    post_amount = 0
            

            colored_generator_title_msg = PrintColor("GENERATOR", Fore.YELLOW)
            print(f"{newline}  <===[{colored_generator_title_msg}]===>")
            generated_passwords = generate_password(check_setting, user_stats=user_stats, amount=post_amount)
            
            ratings: list[str] = []
            for p in generated_passwords:
                ratings.append(rate_password(passwd=p, checkmode=check_setting, user_stats=user_stats, verbose=False, cm_bypass=True))
            
            if len(generated_passwords) < 6:
                for i, p in enumerate(generated_passwords):
                    print(f" * Password {i+1} => {p}")
            
            else:
                DebugMsg("warn", "Number of generated passwords is too large. Saving results...", True, True)
                
                for i, p in enumerate(generated_passwords):
                    save_result(p, check_setting, ratings[i][2], ratings[i][1], DATE_TODAY)
                
                DebugMsg("load-ok", "Genereated passwords info saved successfully.", False, True)

            list_options(1, True)
            choice = retry_query(True)

            if choice == 0:
                logger.info("Leaving to home menu...")
                
                return
            
            elif choice == 1:
                logger.info("Retrying password generator...")
                clr_scr()
                continue
            
            elif choice == 9:
                logger.info("Leaving generator submenu...")
                clr_scr()
                check_setting = None
                continue

            clr_scr()
            check_setting = None

        except Exception:
            logger.exception("Exception found: ")
            DebugMsg("error", "An unexpected error occurred: 'display_password_generator_menu' in 'menus.py'.", True, True)
            DebugInput("warn", "Press Enter to return to password generator.", False, True)
            continue

        finally:
            if user_stats is not None:
                user_stats["total_sessions_seconds"] += time.perf_counter() - loop_start
                logger.info("Successfully updated user stats")


def display_changelog_menu( clear: bool ):
    """Displays changelog menu content."""
    
    logger.info("'display_changelog_menu' executed.")

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
        colored_note_title_msg = PrintColor("NOTE", Fore.YELLOW)
        print(f"{newline}  <===[{colored_note_title_msg}]===>")
        DebugMsg("warn", "Only the 2 most recent updates are shown here", False, True)
        DebugMsg("warn", f"Refer to '{repo_link}' for the full changelog", False, True)
        
        # options
        build_box("top", length=22)
        list_options(2, False, 0)
        build_box("bot", length=22)
    
    except Exception:
        logger.exception("Exception found: ")
        DebugMsg("error", "An unexpected error occurred: 'display_changelog_menu' in 'menus.py'.", True, True)
    

def display_help_menu( clear: bool ):
    """Displays help menu content."""
    
    logger.info("'display_help_menu' executed.")

    display_global_header(clear)
    display_menu_title(4)
    
    # menu content

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
    DebugMsg("warn", "Terminal arguments can only be used outside this user interface\n \t\b You can use the following tags when executing this tool:", False, True)
    
    display_mini_sub_text("'-h/--help' - List argument tags, their descriptions and use-case examples", True)
    display_mini_sub_text("'version' - Display the tool's current version information", True)
    
    display_mini_sub_text("'check -p [password]' - The password to check", True)
    display_mini_sub_text("'-m' - Mode of choice (1, 2 or 3)")
    display_mini_sub_text("'-f' - Check password from file")
    display_mini_sub_text("Example: password_checker_py check -p [PASSWORD (ex: 'test123')] -m [MODE (ex: 1)]")
    
    display_mini_sub_text("generate' - Generates a password", True)
    display_mini_sub_text("Example: password_checker_py generate -m [MODE (ex: 2)]")

    display_mini_sub_text("'-o/--output' - Saves results in a file (JSON)", True)
    display_mini_sub_text("Example: password_checker_py generate -m [MODE (ex: 3)] -o [OUTPUT file-name (ex: 'pizza')]")
    display_mini_sub_text("Example: password_checker_py check -f [filename (ex: pizza)]")

    
    DebugMsg("warn", "NOTE: This tool is still under development", True, True)

    list_options(3, True)


def display_info_menu( user_stats: dict=None ):
    """Displays info menu content"""
    
    logger.info("'display_info_menu' executed.")

    display_global_header(True)
    render_menu_header(5)

    display_mini_title("WELCOME", Fore.YELLOW)
    display_mini_sub_text("Welome to 'password_checker'!")
    display_mini_sub_text("This tool is a prototype scripted in Python, but the real tool will be written in C and/or C++.")
    display_mini_sub_text(f"For future updates, refer to this GitHub repository: '{repo_link}'.")

    display_mini_title("VERSION", Fore.LIGHTGREEN_EX)
    display_version_info()

    display_mini_title("STATISTICS", Fore.LIGHTBLUE_EX)
    display_user_stats(user_stats=user_stats)

    DebugMsg("warn", "NOTE: This tool is still under development", True, True)

    list_options(5, True, exclude_key=0)






# ======== Sub-Menus ======== #

def display_changelog_submenu( user_stats: dict=None ):
    """Submenu for changelog menu. Allows viewing recent or all updates. Has its own loop."""
    
    logger.info("'display_changelog_submenu' executed.")

    while True:
        loop_start = time.perf_counter()
        
        try:
            display_changelog_menu(clear=True)
            
            choice = choose_menu(easter_egg=False, submenu="Changelog")
            
            if choice == 1:
                # display full changelog
                logger.info("Displaying full changelog...")
                display_global_header(True)

                display_menu_title(3, "Full Changelog")
                show_updates(latest_only=False)

                logger.info("Full changelog displayed.")
                DebugMsg("warn", "End of changelog.", True, True)
                DebugInput("tip", "Press Enter to return to changelog menu...", True, True)
            
            elif choice == 9:
                # exit sub-menu
                logger.info("Leaving changelog submenu...")
                clr_scr()
                
                break
            
            else:
                # stay in current menu
                logger.debug("Invalid option: changelog submenu.")
                DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
                DebugInput("tip", "Type Enter to continue...", False, True)
        
        except Exception:
            logger.exception("Exception found: ")
            DebugMsg("error", "An unexpected error occurred: 'display_changelog_submenu' in 'menus.py'.", True, True)
        
        finally:
            if user_stats is not None:
                user_stats["total_sessions_seconds"] += time.perf_counter() - loop_start
                logger.info("Successfully updated user stats")


def display_help_submenu( user_stats: dict=None ):
    """Submenu for help menu. Has its own loop."""
    
    logger.info("'display_help_submenu' executed.")

    while True:
        loop_start = time.perf_counter()
        
        try:
            # start submenu loop
            display_help_menu(True)
            
            choice = choose_menu(easter_egg=False, submenu="Help")
            logger.info("Menu chosen = %d", choice)

            if choice == 9:
                # exit sub-menu
                logger.info("Leaving help submenu...")
                clr_scr()
                break
            
            # stay in current menu
            logger.debug("Invalid option -> help submenu.")
            DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
            DebugInput("tip", "Type Enter to continue...", False, True)
        
        except Exception:
            logger.exception("Exception found: ")
            DebugMsg("error", "An unexpected error occurred: 'display_help_submenu' in 'menus.py'.", True, True)

        finally:
            if user_stats is not None:
                user_stats["total_sessions_seconds"] += time.perf_counter() - loop_start
                logger.info("Successfully updated user stats")


def display_info_submenu( stats: dict=None ):
    """Submenu for info menu. Has its own loop."""
    
    logger.info("'display_info_submenu' executed.")

    while True:
        loop_start = time.perf_counter()
        
        try:
            display_info_menu(user_stats=stats)

            choice = choose_menu(submenu="Info", timeout_s=15.0)
            logger.info("Menu chosen = %d", choice)

            if choice is None:
                raise TimeoutOccurred

            elif choice == 9:
                # exit submenu
                logger.info("Leaving info submenu...")
                clr_scr()
                break

            # stay in current menu
            logger.debug("Invalid option -> info submenu")
            DebugMsg("error", "Invalid option: Please input a listed menu!", False, True)
            DebugInput("tip", "Type Enter to continue...", False, True)

        except TimeoutOccurred:
            continue
        
        finally:
            if stats is not None:
                stats["total_sessions_seconds"] += time.perf_counter() - loop_start
                logger.info("Successfully updated user stats")

