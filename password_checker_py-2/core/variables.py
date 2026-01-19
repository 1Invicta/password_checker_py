# [ variables.py ] #


# ======== Setup ======== #

lc = 'abcdefghijklmnopqrstuvwxyz'
uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = '0123456789'
s = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

MIN_LEN = {1: 8, 2: 12, 3: 16}
MIN_LEN1 = 8
MIN_LEN2 = 12
MIN_LEN3 = 16

MIN_NUM = {1: 2, 2: 3, 3: 5}
MIN_NUM1 = 2
MIN_NUM2 = 3
MIN_NUM3 = 5

MIN_SPL = {1: 1, 2: 3, 3: 4}
MIN_SPL1 = 1
MIN_SPL2 = 3
MIN_SPL3 = 4

MIN_REP = {1: 8, 2: 6, 3: 4}
MAX_REP1 = 8
MAX_REP2 = 6
MAX_REP3 = 4

MIN_ENT = {1: 25, 2: 60, 3: 100}
MIN_ENT1 = 25
MIN_ENT2 = 60
MIN_ENT3 = 100

cl = False
cc = False
cd = False
cs = False
cp = False
cw = False
ce = False

feedback_msgs = {
    1: "Congratulations! Your password is safe.",
    0: "Your password is alright, but you can make it stronger.",
   -1: "Your password is weak! Make it stronger, add digits and special characters."
}