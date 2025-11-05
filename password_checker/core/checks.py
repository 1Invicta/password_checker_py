# [ checks.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import math
from pathlib import Path
from colorama import Fore

# [ Modules ] #
from core.variables import *
from core.utils import DebugMsg, PrintColor

# [ Wordlists ] #
base_dir = Path(__file__).resolve().parent.parent

wordlists_dir = base_dir / "data" / "wordlists"
file1_dir = wordlists_dir / "10k-most-common.txt"
file2_dir = wordlists_dir / "100k-most-used-passwords-NCSC.txt"

with open(file1_dir, 'r', encoding='utf-8') as f:
    COMMON_10K = set(f.read().splitlines())

with open(file2_dir, 'r', encoding='utf-8') as f:
    COMMON_100K = set(f.read().splitlines())






# ======== Checks ======== #

def check_len(passwd: str, type: int=0):
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
        DebugMsg("error", "An unexpected error occurred: 'check_len' in 'checks.py'.", True, True)
        return 0


def check_case(passwd: str, type: int=0):
    """Checks for upper and lowercases in the password."""
    global cc

    DebugMsg("fix", "Chekcing cases...", True, True)
    try:
        uc = any(c.isupper() for c in passwd)
        lc = any(c.islower() for c in passwd)
        
        if type == 1:
            if uc or lc:
                DebugMsg("load-ok", f"{"Uppsercase" if uc else "Lowercase"} found", False, True)
                cc = False
                return 1
            DebugMsg("error", f"Upper and/or lower case not found", False, True)
            cc = True
            return 0
        
        elif 2 <= type:
            if uc and lc:
                DebugMsg("load-ok", f"Upper and lower case found", False, True)
                cc = False
                return 1
            DebugMsg("error", f"Upper and/or lower case not found", False, True)
            return 0
        
        else:
            cc = True
            return 0
        
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_case' in 'checks.py'.", True, True)
        return 0


def check_digit(passwd: str, type: int=0):
    """Checks for digits in the password."""
    global cd

    DebugMsg("fix", "Chekcing digits...", True, True)
    try:
        td = 0
        for c in passwd:
            if c.isdigit():
                td += 1
        
        if type == 1:
            DebugMsg(f"{"load-ok" if td>=MIN_NUM1 else "error"}", f"Digits: {td}", False, True)
            if td >= MIN_NUM1: cd=False; return 1
            else: cd=True; return 0
        
        elif type == 2:
            DebugMsg(f"{"load-ok" if td>=MIN_NUM2 else "error"}", f"Digits: {td}", False, True)
            if td >= MIN_NUM2: cd=False; return 1
            else: cd=True; return 0
        
        elif type == 3:
            DebugMsg(f"{"load-ok" if td>=MIN_NUM3 else "error"}", f"Digits: {td}", False, True)
            if td >= MIN_NUM3: cd=False; return 1
            else: cd=True; return 0

    except:
        DebugMsg("error", "An unexpected error occurred: 'check_digit' in 'checks.py'.", True, True)
        return 0


def check_special(passwd: str, type: int=0):
    """Checks for special characters in the password."""
    global cs

    DebugMsg("fix", "Checking for special characters...", True, True)
    try:
        ts = 0
        for c in passwd:
            if not c.isalnum():
                ts += 1

        if type == 1:
            DebugMsg(f"{"load-ok" if ts>=MIN_SPL1 else "error"}", f"Special characters: {ts}", False, True)
            if ts>=MIN_SPL1: cs=False; return 1
            else: cs=True; return 0
        
        elif type == 2:
            DebugMsg(f"{"load-ok" if ts>=MIN_SPL2 else "error"}", f"Special characters: {ts}", False, True)
            if ts>=MIN_SPL2: cs=False; return 1
            else: cs=True; return 0
        
        elif type == 3:
            DebugMsg(f"{"load-ok" if ts>=MIN_SPL3 else "error"}", f"Special characters: {ts}", False, True)
            if ts>=MIN_SPL3: cs=False; return 1
            else: cs=True; return 0
        
        else: cs=True; return 0
        
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_special' in 'checks.py'.", True, True)
        return 0


def check_pattern(passwd: str, type: int=0):
    """Checks for patterns in the password."""
    global cp
    
    try:
        DebugMsg("fix", "Checking for patterns...", True, True)
        DebugMsg(f"{"load-ok" if passwd not in (passwd+passwd)[1:-1] else "error"}", f"{"Pattern not found." if passwd not in (passwd + passwd)[1:-1] else "Pattern found!"}", False, True)
        if passwd not in (passwd+passwd)[1:-1]: cp = False
        else: cp = True
        return 0 if passwd in (passwd + passwd)[1:-1] else 1
    
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_pattern' in 'checks.py.", True, True)


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
        DebugMsg("error", "An unexpected error occurred: 'check_seclist' in 'checks.py'.", True, True)
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

        # count potential character set (R/r)
        r = 0
        if any(c in lc for c in passwd): r += len(lc)
        if any(c in uc for c in passwd): r += len(uc)
        if any(c in d for c in passwd): r += len(d)
        if any(c in s for c in passwd): r += len(s)
        
        # fallback to unique characters
        if r == 0:
            r = len(set(passwd))
        
        L = len(passwd)

        if r == 0: return 0
        
        entropy = L * math.log2(r)

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
            else: ce=True; return 0
            
        else:
            DebugMsg("error", f"Entropy: [{rounded_entropy}]", False, True)
            return 0
    except:
        DebugMsg("error", "An unexpected error occurred: 'check_entropy' in 'checks.py'.", True, True)
        return 0






# ======== Result ======== #

def rate_password(passwd: str, check_list_arg: int=0):
    """Rates the password based on various checks."""
    try:
        checks = [check_len, check_case, check_digit, check_special, check_pattern, check_seclist, check_entropy]
        results = [func(passwd, check_list_arg) for func in checks]
        
        DebugMsg("fix", "Rating password...", True, True)
        total = sum(results)

        score = round(total / len(checks), 2)
        DebugMsg("load-ok", "Calculated rating", False, True)

        if 0.8 <= score:
            return 1, f"[{PrintColor("Strong", Fore.GREEN)}]", score
        elif 0.5 <= score < 0.8:
            return 0, f"[{PrintColor("Moderate", Fore.YELLOW)}]", score
        else:
            return -1, f"[{PrintColor("Weak", Fore.RED)}]", score
    
    except:
        DebugMsg("error", "An unexpected error occurred: 'rate_password' in 'checks.py'.", True, True)
        return 0, f"[{PrintColor("Error", Fore.LIGHTRED_EX)}]", score

