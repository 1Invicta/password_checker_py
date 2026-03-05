# [ utils.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import         sys
import  subprocess
import    platform
import          re

from colorama import Fore, Style




# ======== Utils ======== #

def PrintColor( text: str, color=Fore.WHITE, style=Style.NORMAL ):
    """Custom print with Fore and Style using 'colorama'.
    \n* text: Text to color\n* color: Foreground color
    \n* style: Text style (BRIGHT, NORMAL or DIM)"""

    return f"{color}{style}{text}{Style.RESET_ALL}"


def DebugMsg( type: str, msg: str, newline: bool, wish_print: bool ):
    """Creates a custom debug message.
    \nTypes: 'error', 'warn', 'added', 'fix', 'removed', 'updated', 'tip', 'info', 'load-ok' and 'query'.
    \n* newline: Insert newline before debug input.
    \n* wish_print: True = prints result | False = returns value (Useful for formatting)."""

    pre = "\n " if newline else ''

    if type.lower() == "error":
        if wish_print: print(f" {pre} [{Fore.RED}!{Fore.RESET}] - {msg}")

        return f" {pre} [{Fore.RED}!{Fore.RESET}] - {msg}"
    
    elif type.lower() == "warn":
        if wish_print: print(f" {pre} [{Fore.YELLOW}!{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.YELLOW}!{Fore.RESET}] - {msg}"
    
    elif type.lower() == "added":
        if wish_print: print(f" {pre} [{Fore.GREEN}+{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.GREEN}+{Fore.RESET}] - {msg}"
    
    elif type.lower() == "fix":
        if wish_print: print(f" {pre} [{Fore.YELLOW}/{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.YELLOW}/{Fore.RESET}] - {msg}"
    
    elif type.lower() == "removed":
        if wish_print: print(f" {pre} [{Fore.RED}-{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.RED}-{Fore.RESET}] - {msg}"
    
    elif type.lower() == "updated":
        if wish_print: print(f" {pre} [{Fore.RED}UPDATED{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.RED}UPDATED{Fore.RESET}] - {msg}"
    
    elif type.lower() == "tip":
        if wish_print: print(f" {pre} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}"
    
    elif type.lower() == "info":
        if wish_print: print(f" {pre} [{Fore.LIGHTYELLOW_EX}INFO{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.LIGHTYELLOW_EX}INFO{Fore.RESET}] - {msg}"

    elif type.lower() == "load-ok":
        if wish_print: print(f" {pre} [{Fore.GREEN}OK{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.GREEN}OK{Fore.RESET}] - {msg}"
    
    elif type.lower() == "query":
        if wish_print: print(f" {pre} [{Fore.LIGHTYELLOW_EX}?{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.LIGHTYELLOW_EX}?{Fore.RESET}] - {msg}"
    
    if wish_print: print(f" {pre} [{Fore.CYAN}pssw_chkr{Fore.RESET}] - {msg}")
    
    return f" {pre} [{Fore.LIGHTYELLOW_EX}System{Fore.RESET}] - {msg}"


def DebugInput( type: str, msg: str, newline: bool, wish_print: bool ):
    """Display debug input.\n* Types: 'tip' and 'warn'\n* newline: Insert newline before debug input
    \n* wish_print: True prints the result and returns the value; False returns the value"""

    pre = "\n " if newline else ''

    if type.lower() == "tip":
        if wish_print: input(f" {pre} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}"
    
    elif type.lower() == "warn":
        if wish_print: input(f" {pre} [{Fore.YELLOW}!{Fore.RESET}] - {msg}")
        
        return f" {pre} [{Fore.YELLOW}!{Fore.RESET}] - {msg}"

    if wish_print: input(f" {pre} [{Fore.LIGHTYELLOW_EX}{type}{Fore.RESET}] - {msg}")
    
    return f" {pre} [{Fore.LIGHTYELLOW_EX}{type}{Fore.RESET}] - {msg}"


def clr_scr():
    """Clears terminal using 'os' library.\nAdapts to user OS."""

    #os.system("cls" if os.name == "nt" else "clear")
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell=True)


def cmd_title( title: str ):
    """Sets the terminal"""

    if platform.system() == "Windows":
        #os.system(f"title {title}")
        title_cmd = f"title {title}"
        #subprocess.run([title_cmd, "cmd.exe"], shell=True)

    else:
        #os.system(f"\033]0;{title}\007")
        #subprocess.run(f"\033]0;{title}\007", shell=False)
        pass


def display_latest_update( lastUpdate: str, version: str, isLatestUpdate: bool ):
    """Displays the latest update date."""

    newline = "\n"
    print(f"{newline} * {lastUpdate} - [{Fore.LIGHTGREEN_EX if isLatestUpdate else Fore.GREEN}ver-{version}{Style.RESET_ALL}]")


def display_current_version( current_ver: str ):
    """Displays the current tool version."""

    newline = "\n"
    
    version_msg = f"version-{current_ver}"
    colored_version_msg = PrintColor(version_msg, Fore.GREEN, Style.BRIGHT)
    
    print(f"{newline} <Current>: [{colored_version_msg}]")


def strip_ansi( text: str ) -> str:
    """Strips 'text' from ANSI codes."""

    return re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', text)


def fit_in_header_box( text: str, box_width: int=29, suffix: str='...', fill_char: str=' ' ) -> str:
    """Fits text within the header box while accounting for ANSI codes."""
    
    visible = strip_ansi(text)
    border_len = len(" | ") + len("|")
    inner_width = box_width - border_len

    if len(visible) > inner_width:
        visible = visible[:inner_width - len(suffix)] + suffix

    padding = fill_char * max(inner_width - len(strip_ansi(visible)), 0)
    
    return f"{visible}{Style.RESET_ALL}{padding}"


def inner_color_brackets( text: str, color=Fore.WHITE, style=Style.NORMAL ) -> str:
    """Colors text within brackets, keeps the default bracket style."""
    
    if not (text.startswith('[') and text.endswith(']')):
        return PrintColor(text, color, style)
    
    return f"[{PrintColor(text[1:-1], color, style)}]"


exit_msg = DebugMsg("error", "Closing", True, False)


def QuitTool():
    """Quits program."""
    
    clr_scr()
    print(exit_msg)
    sys.exit(0)

