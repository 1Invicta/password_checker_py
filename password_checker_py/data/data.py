# [ variables.py ] #


from datetime import datetime

# ======== Setup ======== #

# CURRENT DATE
DATE_TODAY = datetime.today().strftime("%Y-%m-%d")


# ALPHANUMERICAL SETS
lc = 'abcdefghijklmnopqrstuvwxyz'
uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = '0123456789'
s = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


# MINIMUM REQUIREMENTS
MIN_LEN = {1: 8, 2: 12, 3: 16}
MIN_NUM = {1: 2, 2: 3, 3: 5}
MIN_SPL = {1: 1, 2: 3, 3: 4}
MIN_REP = {1: 8, 2: 6, 3: 4}
MIN_ENT = {1: 25, 2: 60, 3: 100}


# BOOLEAN CHECK FLAGS
cl = False
cc = False
cd = False
cs = False
cp = False
cw = False
ce = False


# BASIC FEEDBACK
feedback_msgs = {
    1: "Congratulations! Your password is safe.",
    0: "Your password is alright, but you can make it stronger.",
   -1: "Your password is weak! Make it stronger by adding digits and special characters."
}


# VISUALS LIMITS
BOX_LENGTH = 35