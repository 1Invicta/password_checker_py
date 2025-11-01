#______ [utils] _____ #


# =================== #
# ====== Setup ====== #
# =================== #

# ---- Libs ---- #
import os, re
from colorama import Fore, Style

# --- Visual --- #
header_box = " #--------------------------#"



# =================== #
# ====== Utils ====== #
# =================== #

def PrintColor(text: str, color=Fore.WHITE, style=Style.NORMAL):
    """Custom print with Fore and Style using 'colorama'.\n* text: Text to color\n* color: Foreground color\n* style: Text style (BRIGHT, NORMAL or DIM)"""
    return f"{color}{style}{text}{Style.RESET_ALL}"


def DebugMsg(type: str, msg: str, newline: bool, wish_print: bool):
    """Display debug message.
    \nTypes: 'error', 'warn', 'added', 'fix', 'removed', 'updated', 'tip' and 'info'.
    \n* newline: Insert newline before debug input.
    \n* wish_print: True = prints result | False = returns value (Useful for formatting)."""

    if type.lower() == 'error':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.RED}!{Fore.RESET}] - {msg}")
        return f" {' \n ' if newline else ''} [{Fore.RED}!{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'warn':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.YELLOW}!{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.YELLOW}!{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'added':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.GREEN}+{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.GREEN}+{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'fix':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.YELLOW}/{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.YELLOW}/{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'removed':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.RED}-{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.RED}-{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'updated':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.RED}UPDATED{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.RED}UPDATED{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'tip':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'info':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}INFO{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}INFO{Fore.RESET}] - {msg}"

    elif type.lower() == 'load-ok':
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.GREEN}OK{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.GREEN}OK{Fore.RESET}] - {msg}"
    
    else:
        if wish_print: print(f" {'\n ' if newline else ''} [{Fore.CYAN}pssw_chkr{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}System{Fore.RESET}] - {msg}"


def DebugInput(type: str, msg: str, newline: bool, wish_print: bool):
    """Display debug input.\n* Types: 'tip' and 'warn'\n* newline: Insert newline before debug input
    \n* wish_print: True prints the result and returns the value; False returns the value"""

    if type.lower() == 'tip':
        if wish_print: input(f" {'\n' if newline else ''} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}TIP{Fore.RESET}] - {msg}"
    
    elif type.lower() == 'warn':
        if wish_print: input(f" {'\n' if newline else ''} [{Fore.YELLOW}!{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.YELLOW}!{Fore.RESET}] - {msg}"

    else:
        if wish_print: input(f" {'\n' if newline else ''} [{Fore.LIGHTYELLOW_EX}{type}{Fore.RESET}] - {msg}")
        return f" {'\n ' if newline else ''} [{Fore.LIGHTYELLOW_EX}{type}{Fore.RESET}] - {msg}"


def clr_scr():
    """Clears terminal using 'os' library.\nAdapts to user OS."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        DebugMsg("error", "An error occurred: 'clr_scr', line 90 at 'utils.py'.", True, True)


def cmd_title(title: str):
    try:
        os.system(f"title {title}")
    except:
        DebugMsg("error", "An error occurred: 'cmd_title', line 98 at 'utils.py'.", True, True)


def display_latest_update(lastUpdate: str, version: str, isLatestUpdate: bool):
    try:
        print(f"\n * {lastUpdate} - [{Fore.LIGHTGREEN_EX if isLatestUpdate else Fore.GREEN}ver-{version}{Style.RESET_ALL}]")
    except:
        DebugMsg("error", "An error occurred: 'display_latest_update', line 105 at 'utils.py'.", True, True)


def display_current_version(current_ver: str):
    try:
        print(f"\n <Current>: [{PrintColor(f"version-{current_ver}", Fore.GREEN, Style.BRIGHT)}]")
    except:
        DebugMsg("error", "An error occurred: 'display_current_version', line 112 at 'utils.py'.", True, True)


def strip_ansi(text: str) -> str:
    return re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', text)


def fit_in_header_box(text: str, box_width: int = len(header_box), suffix='...', fill_char=' ') -> str:
    """Fits text within the header box while accounting for ANSI codes."""
    visible = strip_ansi(text)
    border_len = len(" | ") + len("|")
    inner_width = box_width - border_len

    if len(visible) > inner_width:
        visible = visible[:inner_width - len(suffix)] + suffix

    padding = fill_char * max(inner_width - len(strip_ansi(visible)), 0)
    return f"{visible}{Style.RESET_ALL}{padding}"


def inner_color_brackets(text: str, color=Fore.WHITE, style=Style.NORMAL) -> str:
    """Colors text within brackets, keeps the default bracket style."""
    if not (text.startswith('[') and text.endswith(']')):
        return PrintColor(text, color, style)
    return f"[{PrintColor(text[1:-1], color, style)}]"


exit_msg = DebugMsg("error", "Closing", True, False)


def QuitTool():
    """Quits program."""
    clr_scr()
    print(exit_msg)
    return

