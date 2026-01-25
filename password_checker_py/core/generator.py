# [ generator.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import secrets, logging
logger = logging.getLogger(__name__)

# [ Modules ] #
from ..data.data import lc, uc, d, s, MIN_LEN






# ======= Generate ======= #

def generate_password(checkmode: int = 1, verbose: bool=True, user_stats: dict=None):
    from .utils import DebugMsg

    if verbose: DebugMsg("info", "Generating password...", False, True)
    
    if checkmode not in [1, 2, 3]:
        checkmode = 1
    
    REQUIREMENT = MIN_LEN[checkmode]

    # === settings per type === #
    if checkmode == 1:
        charset = lc + uc
    
    elif checkmode == 2:
        charset = lc + uc + d
    
    elif checkmode == 3:
        charset = lc + uc + d + s
    
    # === generate password === #
    password = ''.join(secrets.choice(charset) for _ in range(REQUIREMENT))
    
    user_stats["passwords_generated"] += 1
    
    if verbose: DebugMsg("info", "Password generated.", False, True)

    logger.info("Generated password, check-mode=%d", {checkmode})
    return password

