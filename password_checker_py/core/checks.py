# [ checks.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import                 math
import              logging

logger = logging.getLogger(__name__)

from pathlib  import   Path
from colorama import   Fore

# [ Modules ] #
from ..data import     data
from .utils import     DebugMsg, PrintColor

# [ Wordlists ] #
base_dir = Path(__file__).resolve().parent.parent

wordlists_dir = base_dir / "data" / "wordlists"
file1_dir = wordlists_dir / "10k-most-common.txt"
file2_dir = wordlists_dir / "100k-most-used-passwords-NCSC.txt"

with open(file1_dir, 'r', encoding='utf-8') as f:
    COMMON_10K = set(f.read().splitlines())
    logger.info("'COMMON_10K' wordlist loaded successfully.")

with open(file2_dir, 'r', encoding='utf-8') as f:
    COMMON_100K = set(f.read().splitlines())
    logger.info("'COMMON_100K' wordlist loaded successfully.")



# DIRECT REQUIREMENTS AND ALPHANUMERICAL REFERENCES
MIN_LEN = data.MIN_LEN
MIN_NUM = data.MIN_NUM
MIN_SPL = data.MIN_SPL
MIN_ENT = data.MIN_ENT
lc = data.lc
uc = data.uc
d = data.d
s = data.s




# ======== Checks ======== #

def check_len( passwd: str, checkmode: int=1, verbose: bool=True, *_ ):
    """Checks the length of the password."""

    logger.info("'check_len' executed - checkmode=%d, verbose=%s.", checkmode, verbose)

    global cl

    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"


    if verbose: DebugMsg("fix", "Checking length...", True, True)
    
    length = len(passwd)

    if verbose:
        DebugMsg(
            "load-ok" if MIN_LEN[checkmode] <= length else "error", 
            f"Length: [{length}/{MIN_LEN[checkmode]}]", 
            False, 
            True
        )
    
    if MIN_LEN[checkmode] <= length:
        
        return 1
    
    data.cl=True
    
    return 0


def check_case( passwd: str, checkmode: int=1, verbose: bool=True, *_ ):
    """Checks for upper and lowercases in the password."""

    logger.info("'check_case' executed: checkmode=%d, verbose=%s.", checkmode, verbose)

    global cc

    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"


    if verbose: DebugMsg("fix", "Chekcing cases...", True, True)
    
    uc = any(c.isupper() for c in passwd)
    lc = any(c.islower() for c in passwd)
    
    if checkmode == 1:
        if uc or lc:
            case_found = "Uppercase" if uc else "Lowercase"
            if verbose: DebugMsg("load-ok", case_found + "found", False, True)
            
            return 1
        
        if verbose: DebugMsg("error", "Upper and/or lower case not found", False, True)
        data.cc = True
        
        return 0
    
    elif 2 <= checkmode:
        if uc and lc:
            if verbose: DebugMsg("load-ok", "Upper and lower case found", False, True)

            return 1
        
        if verbose: DebugMsg("error", "Upper and/or lower case not found", False, True)
        
        return 0


def check_digit( passwd: str, checkmode: int=1, verbose: bool=True, *_ ):
    """Checks for digits in the password."""

    logger.info("'check_digit' executed: checkmode=%d, verbose:%s", checkmode, verbose)

    global cd

    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"


    REQUIREMENT = MIN_NUM[checkmode]
    
    if verbose: DebugMsg("fix", "Chekcing digits...", True, True)
    
    tracked_digits = 0
    for c in passwd:
        if c.isdigit():
            tracked_digits += 1
    
    if verbose: 
        DebugMsg(
            "load-ok" if REQUIREMENT<=tracked_digits else "error", 
            f"Digits: {tracked_digits}/{REQUIREMENT}", 
            False, 
            True
        )
    
    if not REQUIREMENT <= tracked_digits:
        data.cd = True
        return 0
    
    return 1


def check_special( passwd: str, checkmode: int=1, verbose: bool=True, *_ ):
    """Checks for special characters in the password."""

    logger.info("'check_special' executed: checkmode=%d, verbose=%s", checkmode, verbose)

    global cs

    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"
    

    REQUIREMENT = MIN_SPL[checkmode]

    if verbose: DebugMsg("fix", "Checking for special characters...", True, True)
        
    track_special = 0
    for c in passwd:
        if not c.isalnum():
            track_special += 1

    if verbose:
        DebugMsg(
            "load-ok" if REQUIREMENT<=track_special else "error", 
            f"Special characters: {track_special}/{REQUIREMENT}", 
            False, 
            True
            )

    if not REQUIREMENT <= track_special:
        data.cs = True
        
        return 0
    
    return 1


def check_pattern( passwd: str, checkmode: int=1, verbose: bool=True, *_ ):
    """Checks for patterns in the password."""

    logger.info("'check_pattern' executed: checkmode=%d, verbose=%s", checkmode, verbose)

    global cp
    
    pattern_check = passwd not in (passwd+passwd)

    if verbose: DebugMsg("fix", "Checking for patterns...", True, True)
    if verbose:
        DebugMsg(
            "load-ok" if pattern_check else "error", 
            "Pattern not found." if pattern_check else "Pattern found!", 
            False, 
            True
        )

    if not pattern_check:
        data.cp = True
        
        return 0

    return 1


def check_seclist( passwd: str, checkmode: int=1, verbose: bool=True, cm_bypass: bool=False, *_ ):
    """Checks if the password is present in one of the wordlists (currently 10k or 100k)."""

    logger.info("'check_seclist' executed: checkmode=%d, verbose=%s", checkmode, verbose)

    global cw

    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"
    

    if checkmode == 1:
        return 0
    
    elif checkmode == 2 or cm_bypass:
        # 10k check => common check
        wordlist = COMMON_10K
        verbose_msg = "Searching in 10k most common passwords..."
        warn_type = "error"
        warn_msg = "ATTENTION: Password found in very common wordlist!"
        
    elif checkmode == 3:
        # 100k check => strong check
        wordlist = COMMON_100K
        verbose_msg = "Searching in 100k most common passwords..."
        warn_type = "warn"
        warn_msg = "ALERT: Password found in common wordlist!"
    
    
    try:
        if verbose: DebugMsg("fix", verbose_msg, True, True)
        
        if passwd in wordlist:
            if verbose: DebugMsg(warn_type, warn_msg, False, True)
            data.cw = True

            return -1
        
        if verbose: DebugMsg("load-ok", "Not found", False, True)

        return 0
        
    except Exception:
        logger.warning("Exception found: ", exc_info=True)
        DebugMsg("error", "An unexpected error occurred: 'check_seclist' in 'checks.py'.", True, True)
        return 0


def check_entropy( passwd: str, checkmode: int=1, verbose: bool=True, *_ ):
    """Uses an approximation to Shannon's Theorem to determine the password's entropy in bits.
    \nChange the minimum requirement with the 'checkmode' parameter."""

    logger.info("'check_entropy' executed: checkmode=%d, verbose=%s", checkmode, verbose)

    global ce
    
    assert checkmode in [1, 2, 3], "Invalid 'checkmode'!"
    

    REQUIREMENT = MIN_ENT[checkmode]

    if verbose: DebugMsg("fix", "Checking entropy...", True, True)
        
    r = 0
    if any(c in lc for c in passwd):    r += len(lc)
    if any(c in uc for c in passwd):    r += len(uc)
    if any(c in d for c in passwd):     r += len(d)
    if any(c in s for c in passwd):     r += len(s)
    
    # fallback to unique characters
    if r == 0:
        r = len(set(passwd))

    if r == 0: return 0
    
    entropy = len(passwd) * math.log2(r)

    entropy_check = REQUIREMENT <= entropy
    
    if verbose:
        DebugMsg(
            "load-ok" if entropy_check else "error", 
            f"Entropy: [{entropy:.2f}] bits / [{REQUIREMENT}] bits", 
            False, 
            True
        )
    
    if not entropy_check:
        data.ce = True
        
        return 0
    
    return 1






# ======== Result ======== #

def rate_password( passwd: str, checkmode: int=0, verbose: bool=True, user_stats: dict=None, cm_bypass: bool=False, isGenerator: bool=False ):
    """Rates the password based on various checks."""
    
    logger.info("'rate_password' executed: checkmode=%d, verbose=%s", checkmode, verbose)

    try:
        if user_stats is not None:
            user_stats["total_length_sum"] += len(passwd)
        
        checks = [check_len, check_case, check_digit, check_special, check_pattern, check_seclist, check_entropy]
        results = [func(passwd, checkmode, verbose, cm_bypass) for func in checks]
        
        if verbose: DebugMsg("fix", "Rating password...", True, True)
        
        total = sum(results)
        score = round(total / len(checks), 2)
        
        if user_stats is not None and not isGenerator:
            user_stats["passwords_tested"] += 1
        
        if verbose: DebugMsg("load-ok", "Calculated rating", False, True)

        
        if 0.8 <= score:
            logger.info("Password score: %d", score)
            
            msg = PrintColor("Strong", Fore.GREEN)
            
            if verbose:
                return 1, f"[{msg}]", score

            return 1, "Strong", score
        
        elif 0.5 <= score < 0.8:
            logger.info("Password score: %d", score)

            msg = PrintColor("Moderate", Fore.YELLOW)
            
            if verbose:
                return 0, f"[{msg}]", score
            
            return 1, "Moderate", score
        
        else:
            logger.info("Password score: %d", score)
            
            msg = PrintColor("Weak", Fore.RED)
            
            if verbose:
                return -1, f"[{msg}]", score
            
            return 1, "Weak", score
    
    except:
        logger.warning("Exception found: ", exc_info=True)

        DebugMsg("error", "An unexpected error occurred: 'rate_password' in 'checks.py'.", True, True)
        score = "An error occured!"
        msg = PrintColor("Error", Fore.LIGHTRED_EX)
        
        return 0, f"[{msg}]", score

