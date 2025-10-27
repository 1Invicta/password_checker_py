### [utils] ###

# --- [libs] --- #
import os
from colorama import Fore, Style

# // utils // #

# - display - #
def PrintColor(text: str, color=Fore.WHITE, style=Style.NORMAL):
    """Custom print with Fore and Style using colorama."""
    return f"{color}{style}{text}{Style.RESET_ALL}"

def DebugMsg(type: str, msg: str, newline: bool, wish_print: bool):
    if type == 'error':
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.RED}!{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.RED}!{Fore.RESET}] - {msg}"
    
    elif type == 'warn':
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.YELLOW}!{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.YELLOW}!{Fore.RESET}] - {msg}"
    
    elif type == 'added':
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.GREEN}+{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.GREEN}+{Fore.RESET}] - {msg}"
    
    elif type == 'fix':
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.YELLOW}/{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.YELLOW}/{Fore.RESET}] - {msg}"
    
    elif type == 'removed':
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.RED}-{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.RED}-{Fore.RESET}] - {msg}"
    
    elif type == 'updated':
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.RED}UPDATED{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.RED}UPDATED{Fore.RESET}] - {msg}"

    else:
        if wish_print: print(f" {'\n' if newline else ''} [{Fore.CYAN}pssw_chkr{Fore.RESET}] - {msg}")
        return f" {'\n' if newline else ''} [{Fore.CYAN}pssw_chkr{Fore.RESET}] - {msg}"

def clr_scr():
    os.system('cls' if os.name == 'nt' else 'clear')

def cmd_title(title: str):
    os.system(f"title {title}")
