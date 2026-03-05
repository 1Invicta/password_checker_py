# [ generator.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import      secrets
import      logging

logger = logging.getLogger(__name__)

# [ Modules ] #
from ..core.utils   import DebugMsg
from ..data.data    import lc, uc, d, s, MIN_LEN






# ======= Generate ======= #

def generate_password( checkmode: int = 1, verbose: bool=True, user_stats: dict=None, amount: int=0 ) -> list[str]:
    """Generates a random password"""

    if amount <= 0:
        amount = 1

    if verbose: DebugMsg("info", "Generating password...", False, True)
    
    assert checkmode in [1, 2, 3]
    
    
    REQUIREMENT = MIN_LEN[checkmode]

    # === settings per type === #
    if checkmode == 1:
        charset = lc + uc
    
    elif checkmode == 2:
        charset = lc + uc + d
    
    elif checkmode == 3:
        charset = lc + uc + d + s
    
    # === generate password === #
    password_pool: list[str] = []

    for _ in range(amount):
        password = ''.join(secrets.choice(charset) for _ in range(REQUIREMENT))
        
        user_stats["passwords_generated"] += 1
        
        password_pool.append(password)
    
    
    if verbose: DebugMsg("info", "Password generated.", False, True)
    logger.info("Generated password, check-mode=%d", {checkmode})
    
    return password_pool

