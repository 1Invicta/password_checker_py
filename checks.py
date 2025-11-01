#______ [checks] _____#


# =================== #
# ====== Setup ====== #
# =================== #

# --- Libs --- #
import os, math, string
from colorama import Fore, Style

# --- Mods --- #
from utils import DebugMsg, DebugInput, PrintColor

# - Wordlists - #
current_dir = os.getcwd()
data_dir = current_dir + r"\wordlists"
file1_dir = data_dir + r"\10k-most-common.txt"
file2_dir = data_dir + r"\100k-most-used-passwords-NCSC.txt"

with open(file1_dir, 'r', encoding='utf-8') as f:
    COMMON_10K = set(line.strip() for line in f)

with open(file2_dir, 'r', encoding='utf-8') as f:
    COMMON_100K = set(line.strip() for line in f)


# ==================== #
# ====== Checks ====== #
# ==================== #

class Checks():
    pass
def check_len(passwd: str, type=0):
    """Checks the length of the password."""
    print("    * Checking length...")
    length = len(passwd)
    if length >= 8:
        return 1#, f"len:{length}"
    elif 0 < length < 8:
        return .5#, f"len:{length}"
    else:
        return 0#, "len:0"


def check_case(passwd: str, type=0):
    """Checks for upper and lowercases in the password."""
    print("    * Checking characters...")
    uc = any(c.isupper() for c in passwd)
    lc = any(c.islower() for c in passwd)
    if uc and lc:
        return 1#, f"uc:{uc}, lc:{lc}"
    elif uc or lc:
        return .5#, f"uc:{uc}, lc:{lc}"
    else:
        return 0#, "neither"


def check_digit(passwd: str, type=0):
    """Checks for digits in the password."""
    print("    * Checking digits...")
    return 1 if any(c.isdigit() for c in passwd) else 0


def check_special(passwd: str, type=0):
    """Checks for special characters in the password."""
    print("    * Checking special characters...")
    return 1 if any(not c.isalnum() for c in passwd) else 0


def check_seclist(passwd: str, type: int=0):
    """Checks if the password is present in one of the wordlists (currently 10k or 100k)."""
    if type == 2:
        # 10k check => common check
        print("    * Comparing to 10k most common passwords...")
        if passwd in COMMON_10K:
            DebugMsg("error", "ATTENTION: Password found in very common database!", True, True)
            return -1
        return 0
    
    elif type == 3:
        # 100k check => strong check
        print("    * Comparing to 100k most common passwords...")
        if passwd in COMMON_100K:
            DebugMsg("warn", "ALERT: Password found in common database!", True, True)
            return -1
        return 1
    
    else:
        return 0


def check_entropy(passwd: str):
    """Uses Shannon's Theorem"""
    # character sets
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    d = string.digits
    s = string.punctuation

    # character pool
    char_pool = set()
    for c in passwd:
        if c in lc:
            char_pool.update(lc)
        elif c in uc:
            char_pool.update(uc)
        elif c in d:
            char_pool.update(d)
        elif c in s:
            char_pool.update(s)
        else:
            # handle other characters
            char_pool.update(c)

    # count potential character set (R)
    R = 0
    if any(c in lc for c in passwd):
        R += len(lc)
    elif any(c in uc for c in passwd):
        R += len(uc)
    elif any(c in d for c in passwd):
        R += len(d)
    elif any(c in s for c in passwd):
        R += len(s)
    
    # fallback to unique characters
    if R == 0:
        R = len(set(passwd))
    
    L = len(passwd)

    if R == 0:
        return 0
    
    entropy = L * math.log2(R)

    return round(entropy, 2)

#test = input("[TEST] Enter password: ")
#print(f"Password '{test}' has {check_entropy(test)} bits of entropy.")


# ==================== #
# ====== Result ====== #
# ==================== #

def rate_password(passwd: str, check_list_arg=0):
    """Rates the password based on various checks."""
    checks = [check_len, check_case, check_digit, check_special, check_seclist]
    results = [func(passwd, check_list_arg) for func in checks]
    total = sum(results)

    score = total / len(checks)

    if total >= 0.8:
        return 1, f"[{PrintColor("Strong", Fore.GREEN)}]", total
    elif 0.5 <= total < 0.8:
        return 0, f"[{PrintColor("Moderate", Fore.YELLOW)}]", total
    else:
        return -1, f"[{PrintColor("Weak", Fore.RED)}]", total

