# [ visuals.py ] #



# ========= Setup ========= #

# [ Libraries ] #
from colorama import Fore, Style

# [ Modules ] #
from .. data import data
from ..core import checks
from ..core.utils import display_latest_update
from ..data.changelog import changelog
from ..core.utils import clr_scr, DebugMsg, PrintColor

# [ Information ] #
LATEST_VERSION = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]


# ======== Visuals ======== #

header_box = " #--------------------------#"
menu_options_top = "\n #===============#"
menu_options_bot = " #===============#"

logo_v1 = """\t                                      __              __                    
\t    ____  ____ ___________      _____/ /_  ___  _____/ /__      ____  __  __
\t   / __ \/ __ `/ ___/ ___/_____/ ___/ __ \/ _ \/ ___/ //_/_____/ __ \/ / / /
\t  / /_/ / /_/ (__  |__  )_____/ /__/ / / /  __/ /__/ ,< /_____/ /_/ / /_/ / 
\t / .___/\__,_/____/____/      \___/_/ /_/\___/\___/_/|_|     / .___/\__, /  
\t/_/                                                         /_/    /____/   """


# [ Options ] #
menu_options = {
    1: "Check Password",
    2: "Generate Password",
    3: "Changelog",
    4: "Help",
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


# ======= Functions ====== #

def build_box(topORbot: str, length: int=15, wish_print: bool=True):
    """Builds custom-sized options box. Defaults to a size of 15."""
    try:
        newline = "\n"
        top = f"{newline} #{'='*length}#"
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
        DebugMsg("error", f"An unexpected error occurred: 'build_box' in 'visuals.py'.", True, True)


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
        DebugMsg("error", "An unexpected error occurred: 'display_global_header' in 'visuals.py'.", True, True)

def display_menu_title(menu_id: int, override: str='', wish_logo: bool=False):
    """Displays the title for a given menu."""
    try:
        newline = "\n"

        titles = {
            0: "/Home",
            1: "/password_checker_py",
            2: "/password_generator",
            3: "/Changelog",
            4: "/Help"
        }
        title = titles.get(menu_id, "/")
        if not override: print(f"{newline}<===[{title}]===>")
        if override: print(f"{newline}<===[{str(override)}]===>")
        if wish_logo: print(logo_v1)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'display_menu_title' in 'visuals.py'.", True, True)

def display_mini_title(title: str, color=Fore.WHITE, style=Style.BRIGHT, custom_index: int=0):
    """Displays a mini-title with Fore and Style using 'colorama'.
    \n* text: Text to color
    \n* color: Foreground color
    \n* style: Text style (BRIGHT, NORMAL or DIM)"""

    newline = "\n"

    if custom_index != 0:
        print(f"{newline}  <[{PrintColor('#'+str(custom_index), Fore.LIGHTGREEN_EX)}] - [{PrintColor(title, color, style)}]>")
    else:
        print(f"{newline}  <===[{PrintColor(title, color, style)}]===>")


def display_mini_sub_text(text: str, newline: bool=False):
    """Displays a mini sub-text."""
    pre = "\n" if newline else ''
    print(f"{pre}   => {text}")


def render_menu_header(menu_id: int, clear: bool=True):
    """Renders the default menu header."""
    try:
        display_global_header(clear)
        display_menu_title(menu_id)

    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'render_menu_header' in 'visuals.py'.", True, True)


def list_options(menu_id: int, buildBox: bool, exclude_key: int=-1, boxSize: int = 15):
    """Displays available menus for the selected menu."""
    try:
        if buildBox: build_box("top", length=boxSize)

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
        
        if buildBox: build_box("bot", length=boxSize)
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'list_options' in 'visuals.py'.", True, True)


def list_password_check_modes(isGenerator: bool, write_current_mode: bool = True):
    """Lists password check modes."""
    try:
        newline = "\n"
        if not isinstance(isGenerator, bool):
            DebugMsg("error", "'isGenerator' argument must be a boolean: 'list_password_check_modes' in 'visuals.py'.", False, True)
        
        settings = (
            {
                1: f"{Fore.LIGHTGREEN_EX}Basic {Fore.RESET}",
                2: f"{Fore.LIGHTBLUE_EX}Medium{Fore.RESET}",
                3: f"{Fore.LIGHTMAGENTA_EX}Strong{Fore.RESET}"
            }
            if isGenerator == False
            else {
                1: f"{Fore.LIGHTGREEN_EX}Simple  {Fore.RESET}",
                2: f"{Fore.LIGHTBLUE_EX}Balanced{Fore.RESET}",
                3: f"{Fore.LIGHTMAGENTA_EX}Secure  {Fore.RESET}"
            }
        )
        
        if write_current_mode: print(f"{newline} Current mode: [{write_current_check_mode(1, False, isGenerator)}]")


        build_box('t', 16)
        for k, v in settings.items():
            print(f"  [{k}] - [{v}]")
        #print(f"  [9] - [{Fore.RED}BACK{' '*(8-len('BACK'))}{Fore.RESET}]")# // may reuse in the future
        print(f"  [9] - [{Fore.RED}BACK{Fore.RESET}]")
        build_box('b', 16)
     
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'list_password_check_modes' in 'visuals.py'.", True, True)


def write_current_check_mode(setting: int, wish_print: bool=False, isGenerator: bool=False):
    """Returns currently selected check mode for password checking."""
    try:
        newline = "\n"

        if setting == 1:
            if isGenerator == False:
                colored_mode_msg = PrintColor("Basic", Fore.LIGHTGREEN_EX)

                if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")
                return f"{colored_mode_msg}"
            else:
                colored_mode_msg = PrintColor("Simple", Fore.LIGHTGREEN_EX)

                if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")
                return f"{colored_mode_msg}"
        
        elif setting == 2:
            if isGenerator == False:
                colored_mode_msg = PrintColor("Medium", Fore.LIGHTBLUE_EX)

                if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")
                return f"{colored_mode_msg}"
            else:
                colored_mode_msg = PrintColor("Balanced", Fore.LIGHTBLUE_EX)

                if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")
                return f"{colored_mode_msg}"
            
        elif setting == 3:
            if isGenerator == False:
                colored_mode_msg = PrintColor("Strong", Fore.LIGHTMAGENTA_EX)

                if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")
                return f"{colored_mode_msg}"
            else:
                colored_mode_msg = PrintColor("Secure", Fore.LIGHTMAGENTA_EX)

                if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")
                return f"{colored_mode_msg}"
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'write_current_setting' in 'visuals.py'.", True, True)


def show_feedback():
    """Display feedback to improve password."""
    count = 0
    try:
        if data.cl: print("    * Make your password longer.");count+=1
        if data.cc: print("    * Use upper and lowercase characters.");count+=1
        if data.cd: print("    * Add digits.");count+=1
        if data.cs: print("    * Use special characters.");count+=1
        if data.cp: print("    * Avoid patterns in your password.");count+=1
        if data.cw: print("    * Find a less common password.");count+=1
        if data.ce: print("    * Make your password less obvious.");count+=1
        
        if not count: print("    * Well done! No major feedback needed.")
    except:
        return


def show_password_results(password: str, check_setting: int, user_stats=None):
    """Displays password rating and advice based on user iinput."""
    try:
        newline = "\n"
        render_menu_header(1)
        write_current_check_mode(check_setting, True)
        display_menu_title(1, override=PrintColor("Checking password", Fore.YELLOW, Style.BRIGHT))

        rating, desc, score = checks.rate_password(password, check_setting, user_stats=user_stats)

        display_mini_title("RESULTS", Fore.GREEN, Style.BRIGHT)
        display_mini_sub_text(f"This password is {desc}.")
        display_mini_sub_text(f"Rating [{score}]")

        print(f"{newline} {data.feedback_msgs.get(rating, '')}")
    
    except Exception:
        DebugMsg("error", "An unexpected error occurred: 'show_password_results' in 'visuals.py'.", True, True)


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
        DebugMsg("error", "An unexpected error occurred: 'show_updates' in 'visuals.py'.", True, True)