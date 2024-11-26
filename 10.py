# tökéletes szám-oló

be = int(input("Mondj egy számot, megmondom hogy tökéletes-e: "))
ossz = 0
for i in range(1, be):
    if be % i == 0:
        ossz = ossz + i
if ossz == be:
    print("A szám tökéletes!")
else:
    print("A szám nem tökéletes!")