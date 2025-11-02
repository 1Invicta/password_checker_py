#______ [checks] _____#


# =================== #
# ====== Setup ====== #
# =================== #

# --- Libs --- #
import os, math
from colorama import Fore, Style

# --- Mods --- #
from utils import DebugMsg, DebugInput, PrintColor

# - Wordlists - #
current_dir = os.getcwd()
data_dir = current_dir + r"\wordlists"
file1_dir = data_dir + r"\10k-most-common.txt"
file2_dir = data_dir + r"\100k-most-used-passwords-NCSC.txt"

with open(file1_dir, 'r', encoding='utf-8') as f:
    COMMON_10K = set(f.read().splitlines())

with open(file2_dir, 'r', encoding='utf-8') as f:
    COMMON_100K = set(f.read().splitlines())


# - variables - #
lc = 'abcdefghijklmnopqrstuvwxyz'
uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = '0123456789'
s = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

MIN_LEN1 = 8
MIN_LEN2 = 12
MIN_LEN3 = 14

MIN_ENT1 = 25
MIN_ENT2 = 60
MIN_ENT3 = 100

cl = False
cc = False
cd = False
cs = False
cw = False
ce = False



# ==================== #
# ====== Checks ====== #
# ==================== #

def check_len(passwd: str, type=0):
    """Checks the length of the password."""
    global cl

    DebugMsg("fix", "Checking length...", True, True)
    try:
        length = len(passwd)

        if type == 1:
            DebugMsg(f"{"load-ok" if MIN_LEN1<=length else 'error'}", f"Length: [{length}/{MIN_LEN1}]", False, True)
            if MIN_LEN1 <= length: cl=False; return 1
            else: cl=True; return 0
            
        elif type == 2:
            DebugMsg(f"{"load-ok" if MIN_LEN2<=length else 'error'}", f"Length: [{length}/{MIN_LEN2}]", False, True)
            if MIN_LEN2 <= length: cl=False; return 1
            else: cl=True; return 0
            
        elif type == 3:
            DebugMsg(f"{"load-ok" if MIN_LEN3<= length else 'error'}", f"Length: [{length}/{MIN_LEN3}]", False, True)
            if MIN_LEN3 <= length: cl=False; return 1
            else: cl=True; return 0

        else:
            DebugMsg("error", f"No specified length: [{length}]", False, True)
            return 0
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_len', line 50 at 'checks.py'.", True, True)
        return 0


def check_case(passwd: str, type=0):
    """Checks for upper and lowercases in the password."""
    global cc

    DebugMsg("fix", "Chekcing cases...", True, True)
    try:
        uc = any(c.isupper() for c in passwd)
        lc = any(c.islower() for c in passwd)
        if uc and lc:
            DebugMsg("load-ok", f"Upper and lower case found", False, True)
            cc = False
            return 1
        elif uc or lc:
            DebugMsg("load-ok", f"{"Uppsercase" if uc else "Lowercase"} found", False, True)
            cc = True
            return .5
        else:
            DebugMsg("error", f"Upper and/or lower case not found", False, True)
            return 0
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_case', line 56 in 'checks.py'.", True, True)
        return 0


def check_digit(passwd: str, type=0):
    """Checks for digits in the password."""
    global cd

    DebugMsg("fix", "Chekcing digits...", True, True)
    try:
        td = 0
        for c in passwd:
            if c.isdigit():
                td += 1
        DebugMsg(f"{"load-ok" if td>0 else "error"}", f"Digits: {td}", False, True)
        if any(c.isdigit() for c in passwd): cd=False; return 1
        else: cd=True; return 0

    except:
        DebugMsg("error", "An unexpected error occurred: 'check_digit', line 77 in 'checks.py'.", True, True)
        return 0


def check_special(passwd: str, type=0):
    """Checks for special characters in the password."""
    global cs

    DebugMsg("fix", "Checking for special characters...", True, True)
    try:
        ts = 0
        for c in passwd:
            if not c.isalnum():
                ts += 1
        DebugMsg(f"{"load-ok" if ts>0 else "error"}", f"Special characters: {ts}", False, True)
        if any(not c.isalnum() for c in passwd): cs=False; return 1
        else: cs=True; return 0
        
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_special', line 93 in 'checks.py'.", True, True)
        return 0


def check_seclist(passwd: str, type: int=0):
    """Checks if the password is present in one of the wordlists (currently 10k or 100k)."""
    global cw

    try:
        if type == 2:
            # 10k check => common check
            DebugMsg("fix", "Comparing to 10k most common passwords...", True, True)
            if passwd in COMMON_10K:
                DebugMsg("error", "ATTENTION: Password found in very common database!", False, True)
                cw = True
                return -1
            cw = False
            DebugMsg("load-ok", "Not found", False, True)
            return 0
        
        elif type == 3:
            # 100k check => strong check
            DebugMsg("fix", "Comparing to 100k most common passwords...", True, True)
            if passwd in COMMON_100K:
                DebugMsg("warn", "ALERT: Password found in common database!", False, True)
                cw = True
                return -1
            cw = False
            DebugMsg("load-ok", "Not found", False, True)
            return 0
        
        else:
            return 0
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_seclist', line 109 in 'checks.py'.", True, True)
        return 0


def check_entropy(passwd: str, type: int=0):
    """Uses Shannon's Theorem to determine the password's entropy in bits.
    \nChange the minimum requirement with the 'type' argument."""
    global ce
    
    DebugMsg("fix", "Checking entropy...", True, True)
    try:
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
        if any(c in lc for c in passwd): R += len(lc)
        if any(c in uc for c in passwd): R += len(uc)
        if any(c in d for c in passwd): R += len(d)
        if any(c in s for c in passwd): R += len(s)
        
        # fallback to unique characters
        if R == 0:
            R = len(set(passwd))
        
        L = len(passwd)

        if R == 0: return 0
        
        entropy = L * math.log2(R)

        rounded_entropy = round(entropy, 2)

        if type == 1:
            DebugMsg(f"{"load-ok" if 25<=rounded_entropy else "error"}", f"Entropy: [{rounded_entropy}] bits / [{MIN_ENT1}] bits", False, True)
            if 25 <= rounded_entropy: ce=False; return 1
            else: ce=True; return 0
            
        elif type == 2:
            DebugMsg(f"{"load-ok" if 60<=rounded_entropy else "error"}", f"Entropy: [{rounded_entropy}] bits / {MIN_ENT2} bits", False, True)
            if 60 <= rounded_entropy: ce=False; return 1
            else: ce=True; return 0
            
        elif type == 3:
            DebugMsg(f"{"load-ok" if 100<=rounded_entropy else "error"}", f"Entropy: [{rounded_entropy}] bits / {MIN_ENT3} bits", False, True)
            if 100 <= rounded_entropy: ce=False; return 1
            else: ce=True; return 1
            
        else:
            DebugMsg("error", f"Entropy: [{rounded_entropy}]", False, True)
            return 0
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_entropy', line 136 in 'checks.py'.", True, True)
        return 0



# ==================== #
# ====== Result ====== #
# ==================== #

def rate_password(passwd: str, check_list_arg=0):
    """Rates the password based on various checks."""
    try:
        checks = [check_len, check_case, check_digit, check_special, check_seclist, check_entropy]
        results = [func(passwd, check_list_arg) for func in checks]
        
        DebugMsg("fix", "Rating password...", True, True)
        total = sum(results)

        score = round(total / len(checks), 2)
        DebugMsg("load-ok", "Calculated rating", False, True)

        if score >= 0.8:
            return 1, f"[{PrintColor("Strong", Fore.GREEN)}]", score
        elif 0.5 <= score < 0.8:
            return 0, f"[{PrintColor("Moderate", Fore.YELLOW)}]", score
        else:
            return -1, f"[{PrintColor("Weak", Fore.RED)}]", score
    
    except:
        DebugMsg("error", "An unexpected error occurred: 'rate_password', line 209 in 'checks.py'.", True, True)
        return 0, f"[{PrintColor("Error", Fore.LIGHTRED_EX)}]", score

