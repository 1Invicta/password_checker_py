### [checks] ###

# --- Libs --- #
from colorama import Fore, Style

# -- Checks -- #
def check_len(passwd: str):
    """Checks the length of the password"""
    print("   * Checking length...")
    length = len(passwd)
    if length >= 8:
        return 1, f"len:{length}"
    elif 0 < length < 8:
        return .5, f"len:{length}"
    else:
        return 0, "len:0"


def check_case(passwd: str):
    """Checks upper/lowercase usage"""
    print("   * Checking characters...")
    uc = any(c.isupper() for c in passwd)
    lc = any(c.islower() for c in passwd)
    if uc and lc:
        return 1, f"uc:{uc}, lc:{lc}"
    elif uc or lc:
        return .5, f"uc:{uc}, lc:{lc}"
    else:
        return 0, "neither"


def check_digit(passwd: str):
    """Checks for digits"""
    print("   * Checking digits...")
    digits = [c for c in passwd if c.isdigit()]
    if digits:
        return 1, f"dig(s):{digits}"
    else:
        return 0, "none"


def check_special(passwd: str):
    """Checks for special characters"""
    print("   * Checking special characters...")
    specials = [c for c in passwd if not c.isalnum()]
    if specials:
        return 1, f"sc:{specials}"
    else:
        return 0, "none"


def rate_password(passwd: str):
    """Rates password based on different checks"""
    checks = [check_len, check_case, check_digit, check_special]
    total = sum(func(passwd)[0] for func in checks)

    if total == 4:
        return 1, f"[{Fore.GREEN}Strong{Style.RESET_ALL}]", total
    elif 2 < total < 4:
        return 0, f"[{Fore.YELLOW}Moderate{Style.RESET_ALL}]", total
    else:
        return -1, f"[{Fore.RED}Weak{Style.RESET_ALL}]", total
