#___ [checks] ___#


# =================== #
# ====== Setup ====== #
# =================== #

# --- Libs --- #
import os, random
from time import sleep # will make it optional in ver-0.8
from colorama import Fore, Style

# --- Mods --- #
from utils import DebugMsg, PrintColor

# - Wordlists - #
current_dir = os.getcwd()
data_dir = current_dir + r"\wordlists"
file1_dir = data_dir + r"\10k-most-common.txt"
file2_dir = data_dir + r"\100k-most-used-passwords-NCSC.txt"



# ==================== #
# ====== Checks ====== #
# ==================== #

def check_len(passwd: str, type=0):
    """Checks the length of the password"""
    sleep(random.random())
    print("    * Checking length...")
    sleep(random.random())
    length = len(passwd)
    if length >= 8:
        return 1#, f"len:{length}"
    elif 0 < length < 8:
        return .5#, f"len:{length}"
    else:
        return 0#, "len:0"


def check_case(passwd: str, type=0):
    """Checks upper/lowercase usage"""
    sleep(random.random())
    print("    * Checking characters...")
    sleep(random.random())
    uc = any(c.isupper() for c in passwd)
    lc = any(c.islower() for c in passwd)
    if uc and lc:
        return 1#, f"uc:{uc}, lc:{lc}"
    elif uc or lc:
        return .5#, f"uc:{uc}, lc:{lc}"
    else:
        return 0#, "neither"


def check_digit(passwd: str, type=0):
    """Checks for digits"""
    sleep(random.random())
    print("    * Checking digits...")
    sleep(random.random())
    digits = [c for c in passwd if c.isdigit()]
    if digits:
        return 1#, f"dig(s):{digits}"
    else:
        return 0#, "none"


def check_special(passwd: str, type=0):
    """Checks for special characters"""
    sleep(random.random())
    print("    * Checking special characters...")
    sleep(random.random())
    specials = [c for c in passwd if not c.isalnum()]
    if specials:
        return 1#, f"sc:{specials}"
    else:
        return 0#, "none"


def check_seclist(passwd: str, type: int=0):
    if type == 2:
        # 10k check => common check
        print("    * Comparing to 10k most common passwords...")
        with open(file1_dir) as file1:
            if passwd in file1.read():
                DebugMsg("error", "ATTENTION: Password found in very common database!", True, True)
                return -2
            return 0
    
    elif type == 3:
        # 100k check => strong check
        print("    * Comparing to 100k most common passwords...")
        with open(file2_dir) as file2:
            if passwd in file2.read():
                DebugMsg("warn", "ALERT: Password found in common database!", True, True)
                return -1
            return 1
    
    else:
        return 0



# ==================== #
# ====== Result ====== #
# ==================== #

def rate_password(passwd: str, check_list_arg=0):
    """Rates password based on different checks"""
    checks = [check_len, check_case, check_digit, check_special, check_seclist]
    total = sum(func(passwd, check_list_arg) for func in checks)

    if total == 4:
        return 1, f"[{PrintColor("Strong", Fore.GREEN)}]", total
    elif 2 < total < 4:
        return 0, f"[{PrintColor("Moderate", Fore.YELLOW)}]", total
    else:
        return -1, f"[{PrintColor("Weak", Fore.RED)}]", total

