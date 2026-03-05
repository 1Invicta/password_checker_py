# ===================================== #
#         Password Strength Tool        #
# ===================================== #

import os, math
from pathlib import Path
from colorama import Fore, Style
from password_checker_py.data.data import *

def PrintColor(text: str, color=Fore.WHITE, style=Style.NORMAL): # type: ignore
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

# ==================== #
# ===== Constants ==== #
# ==================== #

LC = "abcdefghijklmnopqrstuvwxyz"
UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIALS = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Minimum thresholds by mode
MIN_LEN = {1: 8, 2: 12, 3: 14} # type: ignore
MIN_ENTROPY = {1: 25, 2: 60, 3: 100}

# Weight of each check (sums to 1)
WEIGHTS = {
    "length": 0.20,
    "case": 0.10,
    "digit": 0.10,
    "special": 0.10,
    "wordlist": 0.25,
    "entropy": 0.25
}

base_dir = Path(__file__).resolve().parent.parent

wordlists_dir = base_dir / "data" / "wordlists"
file1_dir = wordlists_dir / "10k-most-common.txt"
file2_dir = wordlists_dir / "100k-most-used-passwords-NCSC.txt"

# ==================== #
# ====== Class ======= #
# ==================== #

class PasswordChecker:
    def __init__(self, mode: int = 1):
        """Initialize with mode: 1=default, 2=advanced, 3=extreme."""
        self.mode = mode
        self.results = {}
        self.wordlists = self._load_wordlists()
    
    def _load_wordlists(self) -> dict[str, str] | None:
        """Load appropriate wordlists depending on mode."""
        wl = {}
        try:
            with open(file1_dir, 'r', encoding='utf-8') as f:
                COMMON_10K = set(f.read().splitlines())
                wl["10k"] = COMMON_10K

            with open(file2_dir, 'r', encoding='utf-8') as f:
                COMMON_100K = set(f.read().splitlines())
                wl["100k"] = COMMON_100K
            
        except FileNotFoundError:
            DebugMsg("warn", "One or more wordlists not found.", True, True)

        return wl

    # ===== Checks ===== #

    def check_length(self, passwd: str) -> float:
        length = len(passwd)
        threshold = MIN_LEN[self.mode]
        passed = length >= threshold
        DebugMsg("fix", f"Checking length [{length}/{threshold}]...", True, True)
        DebugMsg("load-ok" if passed else "error", f"Length check {'passed' if passed else 'failed'}", False, True)
        return 1.0 if passed else 0.0

    def check_case(self, passwd: str) -> float:
        upper = any(c.isupper() for c in passwd)
        lower = any(c.islower() for c in passwd)
        DebugMsg("fix", "Checking case variety...", True, True)
        if upper and lower:
            DebugMsg("load-ok", "Upper and lowercase found", False, True)
            return 1.0
        elif upper or lower:
            DebugMsg("warn", "Only one case type found", False, True)
            return 0.5
        DebugMsg("error", "No alphabetic characters found", False, True)
        return 0.0

    def check_digit(self, passwd: str) -> float:
        count = sum(c.isdigit() for c in passwd)
        DebugMsg("fix", f"Checking digits ({count})...", True, True)
        return 1.0 if count > 0 else 0.0

    def check_special(self, passwd: str) -> float:
        count = sum(not c.isalnum() for c in passwd)
        DebugMsg("fix", f"Checking special characters ({count})...", True, True)
        return 1.0 if count > 0 else 0.0

    def check_wordlist(self, passwd: str) -> float:
        DebugMsg("fix", "Checking wordlists...", True, True)
        if self.mode == 1 or not self.wordlists:
            return 0.0
        if self.mode >= 2 and passwd in self.wordlists.get("10k", set()):
            DebugMsg("error", "Found in 10k list!", False, True)
            return -0.5
        if self.mode == 3 and passwd in self.wordlists.get("100k", set()):
            DebugMsg("error", "Found in 100k list!", False, True)
            return -0.5
        DebugMsg("load-ok", "Not found in any list", False, True)
        return 0.0

    def check_entropy(self, passwd: str) -> float:
        """Compute normalized entropy score."""
        DebugMsg("fix", "Calculating entropy...", True, True)
        charsets = [LC, UC, DIGITS, SPECIALS]
        r = sum(len(cs) for cs in charsets if any(c in cs for c in passwd))
        if r == 0:
            r = len(set(passwd))
        entropy = len(passwd) * math.log2(r)
        min_ent = MIN_ENTROPY[self.mode]
        DebugMsg("load-ok" if entropy >= min_ent else "warn", f"Entropy: {entropy:.2f} bits", False, True)
        # Normalize entropy to [0,1] range
        return min(entropy / (min_ent * 1.5), 1.0)

    # ===== Rating ===== #

    def rate(self, passwd: str):
        """Run all checks, compute weighted score, and classify."""
        DebugMsg("info", "Checking password...", True, True)
        self.results = {
            "length": self.check_length(passwd),
            "case": self.check_case(passwd),
            "digit": self.check_digit(passwd),
            "special": self.check_special(passwd),
            "wordlist": self.check_wordlist(passwd),
            "entropy": self.check_entropy(passwd)
        }

        weighted_sum = sum(self.results[k] * WEIGHTS[k] for k in WEIGHTS)
        total_weight = sum(WEIGHTS.values())
        score = round(weighted_sum / total_weight, 2)

        if score >= 0.8:
            label = PrintColor("Strong", Fore.GREEN), "Strong"
            status = 1
        elif score >= 0.6:
            label = PrintColor("Moderate", Fore.YELLOW), "Moderate"
            status = 0
        else:
            label = PrintColor("Weak", Fore.RED), "Weak"
            status = -1

        DebugMsg("load-ok", f"Final score: {score:.2f}", True, True)
        return status, f"{label[1]}", score




while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" [ THIS IS A TEST ] ")
        print(" (1) Basic\n (2) Advanced\n (3)Extreme\n")

        choice = input("<CMD>: ")
        test = PasswordChecker(int(choice))
        
        pwd = input("Type password: ")
        result = test.rate(pwd)
        print(f"\nScore: {result[2]}")
        print(f"Your password is {result[1]}.")
        
        retry = input("\nRetry? (y/n)").lower().strip()
        if retry == 'y':
            continue
        elif retry == 'n':
            print("\nExit")
            break
    
    except KeyboardInterrupt:
        print("\nExit")
        break
    except ValueError:
        input("\nPlease choose an availble menu!")
        continue


# ANOTHER CLASS
class Checker:
    def __init__(self, mode: int = 1, verbose: bool = True):
        """Initialize with mode: 1=default, 2=advanced, 3=extreme."""
        self.mode = mode
        self.results = {}
        self.verbose = verbose
        self.wordlists = self._load_wordlists()
    
    def _load_wordlists(self) -> dict[str, str] | None:
        """Load appropriate wordlists based on mode."""
        wl = {}
        try:
            with open(file1_dir, 'r', encoding='utf-8') as f:
                COMMON_10K = set(f.read().splitlines())
                wl["10k"] = COMMON_10K
            
            with open(file2_dir, 'r', encoding='utf-8') as f:
                COMMON_100K = set(f.read().splitlines())
                wl["100k"] = COMMON_100K
        
        except FileNotFoundError:
            DebugMsg("warn", "One or more worlists not found.", True, True)
        
        return wl
    
    # ===== Checks ===== #

    def check_length(self, passwd: str) -> float:
        length = len(passwd)
        threshold = MIN_LEN[self.mode]
        passed = length >= threshold
        if self.verbose: DebugMsg("fix", f"Checking length [{length}/{threshold}]...", True, True)
        if self.verbose: DebugMsg("load-ok" if passed else "error", f"Length check {'passed' if passed else 'failed'}", False, True)
        return 1.0 if passed else 0.0

    def check_case(self, passwd: str) -> float:
        upper = any(c.isupper() for c in passwd)
        lower = any(c.islower() for c in passwd)
        if self.verbose: DebugMsg("fix", "Checking case variety...", True, True)
        if upper and lower:
            if self.verbose: DebugMsg("load-ok", "Upper and lowercase found", False, True)
            return 1.0
        elif upper or lower:
            if self.verbose: DebugMsg("warn", "Only one case type found", False, True)
            return 0.5
        if self.verbose: DebugMsg("error", "No alphabetic characters found", False, True)
        return 0.0

    def check_digit(self, passwd: str) -> float:
        count = sum(c.isdigit() for c in passwd)
        if self.verbose: DebugMsg("fix", f"Checking digits ({count})...", True, True)
        return 1.0 if count > 0 else 0.0

    def check_special(self, passwd: str) -> float:
        count = sum(not c.isalnum() for c in passwd)
        if self.verbose: DebugMsg("fix", f"Checking special characters ({count})...", True, True)
        return 1.0 if count > 0 else 0.0

    def check_wordlist(self, passwd: str) -> float:
        if self.verbose: DebugMsg("fix", "Checking wordlists...", True, True)
        if self.mode == 1 or not self.wordlists:
            return 0.0
        if self.mode >= 2 and passwd in self.wordlists.get("10k", set()):
            if self.verbose: DebugMsg("error", "Found in 10k list!", False, True)
            return -0.5
        if self.mode == 3 and passwd in self.wordlists.get("100k", set()):
            if self.verbose: DebugMsg("error", "Found in 100k list!", False, True)
            return -0.5
        if self.verbose: DebugMsg("load-ok", "Not found in any list", False, True)
        return 0.0

    def check_entropy(self, passwd: str) -> float:
        """Compute normalized entropy score."""
        if self.verbose: DebugMsg("fix", "Calculating entropy...", True, True)
        charsets = [LC, UC, DIGITS, SPECIALS]
        r = sum(len(cs) for cs in charsets if any(c in cs for c in passwd))
        if r == 0:
            r = len(set(passwd))
        entropy = len(passwd) * math.log2(r)
        min_ent = MIN_ENT[self.mode]
        if self.verbose: DebugMsg("load-ok" if entropy >= min_ent else "warn", f"Entropy: {entropy:.2f} bits", False, True)
        # Normalize entropy to [0,1] range
        return min(entropy / (min_ent * 1.5), 1.0)

    # ===== Rating ===== #

    def rate(self, passwd: str):
        """Run all checks, compute weighted score, and classify."""
        if self.verbose: DebugMsg("info", "Checking password...", True, True)
        self.results = {
            "length": self.check_length(passwd),
            "case": self.check_case(passwd),
            "digit": self.check_digit(passwd),
            "special": self.check_special(passwd),
            "wordlist": self.check_wordlist(passwd),
            "entropy": self.check_entropy(passwd)
        }

        #weighted_sum = sum(self.results[k] * WEIGHTS[k] for k in WEIGHTS)
        #total_weight = sum(WEIGHTS.values())
        #score = round(weighted_sum / total_weight, 2)
        total = sum(self.results[v] for v in self.results.values())
        score = round(total / len(self.results), 2)

        if score >= 0.8:
            label = PrintColor("Strong", Fore.GREEN), "Strong"
            status = 1
        elif score >= 0.6:
            label = PrintColor("Moderate", Fore.YELLOW), "Moderate"
            status = 0
        else:
            label = PrintColor("Weak", Fore.RED), "Weak"
            status = -1

        if self.verbose: DebugMsg("load-ok", f"Final score: {score:.2f}", True, True)
        return status, label[1], score