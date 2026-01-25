# [ ui_logic.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import logging
logger = logging.getLogger(__name__)

# [ Modules ] #
from ..core.utils import DebugMsg, DebugInput, clr_scr
from .visuals import write_current_check_mode, list_password_check_modes, render_menu_header, list_options



# ======= Functions ====== #
def choose_menu(easter_egg: bool=False, submenu: str=""):
    """Displays cmd-style input."""
    try:
        newline = "\n"
        simulated_dir = '/' + submenu if submenu != '' else ''
        #user_input = input(f"\n<CMD{f"/{submenu}" if submenu != "" else ""}>: ")
        user_input = input(f"{newline}<CMD{simulated_dir}>: ")
        if user_input == '' or not user_input:
            return 0
        elif  easter_egg and user_input in ("1Invicta", "Invicta"):
            DebugInput("tip", "That's me! ", True, True)
            return 0
        try:
            return int(user_input)
        except ValueError:
            return 0

    except Exception as e:
        logger.error(e, exc_info=True)
        DebugMsg("error", "An unexpected error occurred: 'choose_menu' in 'menus.py'.", True, True)
        return 0


def password_options(useGenerator: bool=False, submenu: str = ""):
    """Handles input choice for password check mode."""
    try:
        list_password_check_modes(isGenerator=useGenerator)

        while True:
            choice = choose_menu(easter_egg=False, submenu="password_checker_py" if not submenu else submenu)
            
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
                DebugMsg("warn", f"No available option given: Using [{write_current_check_mode(1, isGenerator=useGenerator)}] settings!", True, True)
                DebugInput("System", "Type Enter to continue...", False, True)
                return 1
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'password_options' in 'menus.py'.", True, True)


def get_password_or_command(isGenerator: bool = False):
    """Returns a tuple (command, password) from user input."""
    try:
        newline = "\n"

        if not isGenerator:
            userinput = input(f"{newline}<CMD/password_checker_py>: ").strip()
            if not userinput:
                DebugMsg("warn", "Empty input. Please enter a password.", False, True)
                DebugInput("tip", "Press Enter to retry...", False, True)
                return None, None
            
            # userinput is either command or password
            try:
                return int(userinput), None
            
            except ValueError:
                return None, userinput
        
        userinput = input(f"{newline}<CMD/password_checker_py>: ").strip()
        if not userinput:
            return None, True
        try:
            return int(userinput), None
        except ValueError:
            return None, userinput
    
    except Exception:
        DebugMsg("error", "An unexpected error occured: 'get_password_or_command' in 'menus.py'.", True, True)


def retry_query(isGenerator: bool = False):
    """Queries user to retry for a password check."""
    try:
        newline = "\n"

        while True:
            user_input = input(f"{newline}<CMD/password_checker_py>: " if not isGenerator else f"{newline}<CMD/checker/generator>")

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
                write_current_check_mode(1, True, isGenerator)
                list_options(1, True)
                continue

    except Exception:
        DebugMsg("error", "An unexpected error occured: 'retry_query' in 'menus.py'.", True, True)
        return 0
