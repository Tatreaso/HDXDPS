# ember itt mar kell randomozni
import random
n = random.randint(1, 1000)
be = int(input("Tippelj egy számot 1 és 1000 között: "))
# nehezitett:
# counter = 0
while be != n:
    if be > n:
        be = int(input("Nem jó! Tippelj egy kisebb számot: "))
        # counter += 1
    elif be < n:
        be = int(input("Nem jó! Tippelj egy nagyobb számot: "))
        # counter += 1
# print(f"Sikeres tipp! {counter} tipp alatt sikerült betippelni!")
# az also printet szedd ki ha halado feladat
print("Sikeres tipp!")