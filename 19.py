# RANDOOOOM

import random
n = 0
be = ""
while be != "N" or "n":
    n = random.randint(1, 6)
    print(n)
    be = str(input("Dobsz újra? Y/N"))