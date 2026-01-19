# [ generator.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import secrets

# [ Modules ] #
from .variables import lc, uc, d, s, MIN_LEN1, MIN_LEN2, MIN_LEN3






# ======= Generate ======= #

def generate_password(type: int = 1, verbose: bool=True):
    from .utils import DebugMsg

    if verbose: DebugMsg("info", "Generating password...", False, True)
    
    if type not in [1, 2, 3]:
        type = 1
    
    # === settings per type === #
    if type == 1:
        charset = lc + uc
        length = MIN_LEN1
    
    elif type == 2:
        charset = lc + uc + d
        length = MIN_LEN2
    
    elif type == 3:
        charset = lc + uc + d +s
        length = MIN_LEN3
    
    # === generate password === #
    password = ''.join(secrets.choice(charset) for _ in range(length))
    if verbose: DebugMsg("info", "Password generated.", False, True)

    return password

