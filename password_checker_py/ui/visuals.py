# [ visuals.py ] #



# ========= Setup ========= #

# [ Libraries ] #
import logging

logger = logging.getLogger(__name__)

from colorama import Fore, Style

# [ Modules ] #
from .. data            import data
from ..core             import checks
from ..core.utils       import display_latest_update
from ..data.changelog   import changelog
from ..core.utils       import clr_scr, DebugMsg, PrintColor

# [ Information ] #
LATEST_VERSION = changelog[-1]["version"]
LATEST_UPDATE_DATE = changelog[-1]["date"]


# ======== Visuals ======== #

header_box =        " #--------------------------#"
menu_options_top =           "\n #===============#"
menu_options_bot =             " #===============#"

logo_v1 = """\t                                      __              __                    
\t    ____  ____ ___________      _____/ /_  ___  _____/ /__      ____  __  __
\t   / __ \/ __ `/ ___/ ___/_____/ ___/ __ \/ _ \/ ___/ //_/_____/ __ \/ / / /
\t  / /_/ / /_/ (__  |__  )_____/ /__/ / / /  __/ /__/ ,< /_____/ /_/ / /_/ / 
\t / .___/\__,_/____/____/      \___/_/ /_/\___/\___/_/|_|     / .___/\__, /  
\t/_/                                                         /_/    /____/   \n"""


# [ Options ] #
menu_options = {
    1: "Check Password",
    2: "Generate Password",
    3: "Changelog",
    4: "Help",
    5: "Info",
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

info_menu_options = {
    0: "Home",
    9: "Back"
}


# ======= Functions ====== #

def build_box( topORbot: str, length: int=15, wish_print: bool=True ):
    """Builds custom-sized options box. Defaults to a size of 15."""
    
    newline = "\n"

    if length > data.BOX_LENGTH+1:
        length = data.BOX_LENGTH+1

    top = f"{newline} #{'='*length}#"
    bot =          f" #{'='*length}#"
    
    if topORbot.lower().startswith('t'):
        if wish_print:
            print(top)
    
        return top
    
    if wish_print:
        print(bot)

    return bot


def display_global_header( clear: bool ):
    """Displays default header."""
    
    if clear: clr_scr()
    
    upper_box = build_box(header_box, length=26, wish_print=False)
    lower_box = build_box(header_box, length=26, wish_print=False)

    tool_title =    PrintColor("password_checker_py", Fore.LIGHTMAGENTA_EX)
    tool_version =  PrintColor(f"ver-{LATEST_VERSION}", Fore.LIGHTGREEN_EX)
    scripted_by =   PrintColor("Scripted by", Fore.LIGHTWHITE_EX, Style.BRIGHT)
    author =        PrintColor("1Invicta", Fore.CYAN, Style.BRIGHT)

    print(
        f" {upper_box}\n"
        f"  | [{tool_title}]    |\n"
        f"  | [{tool_version}] - {LATEST_UPDATE_DATE} |\n"
        f"  | {scripted_by} [{author}]   |\n"
        f" {lower_box}"
    )


def display_menu_title( menu_id: int, override: str='', wish_logo: bool=False ):
    """Displays the title for a given menu."""
    
    newline = "\n"

    titles = {
        0: "/Home",
        1: "/password_checker_py",
        2: "/password_generator",
        3: "/Changelog",
        4: "/Help",
        5: "/Info"
    }
    title = titles.get(menu_id, "/")
    
    if not override:
        print(f"{newline}<===[{title}]===>")
    
    if override:
        print(f"{newline}<===[{str(override)}]===>")
    
    if wish_logo:
        print(logo_v1)


def display_mini_title( title: str, color=Fore.WHITE, style=Style.BRIGHT, custom_index: int=0 ):
    """Displays a mini-title with Fore and Style using 'colorama'.
    \n* text: Text to color
    \n* color: Foreground color
    \n* style: Text style (BRIGHT, NORMAL or DIM)"""

    newline = "\n"

    if custom_index != 0:
        print(f"{newline}  <[{PrintColor('#'+str(custom_index), Fore.LIGHTGREEN_EX)}] - [{PrintColor(title, color, style)}]>")
        
        return
    
    print(f"{newline}  <===[{PrintColor(title, color, style)}]===>")


def display_mini_sub_text( text: str, newline: bool=False ):
    """Displays a mini sub-text."""
    
    pre = "\n" if newline else ''
    print(f"{pre}   => {text}")


def render_menu_header( menu_id: int, clear: bool=True ):
    """Renders the default menu header."""
    
    display_global_header(clear)
    display_menu_title(menu_id)


def list_options( menu_id: int, buildBox: bool, exclude_key: int=-1, boxSize: int=15 ):
    """Displays available menus for the selected menu."""
    
    if buildBox: build_box("top", length=boxSize)

    options = (
        menu_options            if menu_id == 0 else
        password_menu_options   if menu_id == 1 else
        changelog_menu_options  if menu_id == 2 else
        info_menu_options       if menu_id == 5 else
        {9: "Back"}
    )

    for k, v in options.items():
        if k == exclude_key:
            continue

        color = Fore.RED if k == 9 else Fore.WHITE
        print(f"  [{k}] - {PrintColor(v, color)}")
    
    if buildBox: build_box("bot", length=boxSize)


def list_password_check_modes( isGenerator: bool, write_current_mode: bool=True ):
    """Lists password check modes."""
    
    newline = "\n"

    if not isinstance(isGenerator, bool):
        DebugMsg("error", "'isGenerator' argument must be a boolean: 'list_password_check_modes' in 'visuals.py'.", False, True)
    
    basic =     PrintColor("Basic ", Fore.LIGHTGREEN_EX)
    medium =    PrintColor("Medium", Fore.LIGHTBLUE_EX)
    strong =    PrintColor("Strong", Fore.LIGHTMAGENTA_EX)

    simple =    PrintColor("Simple  ", Fore.LIGHTGREEN_EX)
    balanced =  PrintColor("Balanced", Fore.LIGHTBLUE_EX)
    secure =    PrintColor("Secure  ", Fore.LIGHTMAGENTA_EX)
    
    settings = (
        {
            1: basic,
            2: medium,
            3: strong
        }
        if not isGenerator
        else {
            1: simple,
            2: balanced,
            3: secure
        }
    )
    
    if write_current_mode:
        print(f"{newline} Current mode: [{write_current_check_mode(1, False, isGenerator)}]")


    build_box('t', 16)
    
    for k, v in settings.items():
        print(f"  [{k}] - [{v}]")
    print(f"  [9] - [{Fore.RED}BACK{Fore.RESET}]")
    
    build_box('b', 16)


def write_current_check_mode( checkmode: int, wish_print: bool=False, isGenerator: bool=False ):
    """Returns currently selected check mode for password checking."""
    
    newline = "\n"

    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"

    if checkmode == 1:
        if not isGenerator:
            colored_mode_msg = PrintColor("Basic", Fore.LIGHTGREEN_EX)

            if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")

            return f"{colored_mode_msg}"
        
        colored_mode_msg = PrintColor("Simple", Fore.LIGHTGREEN_EX)

        if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")

        return f"{colored_mode_msg}"
    

    elif checkmode == 2:
        if not isGenerator:
            colored_mode_msg = PrintColor("Medium", Fore.LIGHTBLUE_EX)

            if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")

            return f"{colored_mode_msg}"

        colored_mode_msg = PrintColor("Balanced", Fore.LIGHTBLUE_EX)

        if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")

        return f"{colored_mode_msg}"
    

    elif checkmode == 3:
        if not isGenerator:
            colored_mode_msg = PrintColor("Strong", Fore.LIGHTMAGENTA_EX)

            if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")

            return f"{colored_mode_msg}"

        colored_mode_msg = PrintColor("Secure", Fore.LIGHTMAGENTA_EX)

        if wish_print: print(f"{newline} Current mode: [{colored_mode_msg}]")

        return f"{colored_mode_msg}"


def show_feedback():
    """Display feedback to improve password."""
    
    count = 0
    if data.cl: print("    * Make your password longer.");          count+=1
    if data.cc: print("    * Use upper and lowercase characters."); count+=1
    if data.cd: print("    * Add digits.");                         count+=1
    if data.cs: print("    * Use special characters.");             count+=1
    if data.cp: print("    * Avoid patterns in your password.");    count+=1
    if data.cw: print("    * Find a less common password.");        count+=1
    if data.ce: print("    * Make your password less obvious.");    count+=1
    
    if not count: print("    * Well done! No major feedback needed.")


def show_password_results( password: str, check_setting: int, user_stats=None ):
    """Displays password rating and advice based on user iinput."""
    
    newline = "\n"

    render_menu_header(1)
    write_current_check_mode(check_setting, True)
    display_menu_title(1, override=PrintColor("Checking password", Fore.YELLOW, Style.BRIGHT))

    rating, desc, score = checks.rate_password(password, check_setting, user_stats=user_stats)

    display_mini_title("RESULTS", Fore.GREEN, Style.BRIGHT)
    display_mini_sub_text(f"This password is {desc}.")
    display_mini_sub_text(f"Rating [{score}]")

    print(f"{newline} {data.feedback_msgs.get(rating, '')}")


# for changelog menu
def show_updates( latest_only: bool=True, count: int=3 ):
    """Display 3 latest updates from changelog, optionally as many as wished."""

    ordered = list(reversed(changelog))                             # reverse update list order, start from the "bottom"
    updates_to_show = ordered[:count] if latest_only else ordered   # dynamically show all or part of the changelog

    for update in updates_to_show:
        display_latest_update(update["date"], update["version"], True if update["version"] == LATEST_VERSION else False)
        
        for change_type, msg in update["changes"]:
            DebugMsg(change_type, msg, False, True)

