# szamolvaso bűvösprogram

be = int(input("Mondj egy számot: "))
counter = 0
ossz = 0
legnagyobb = 0
while be != 0:
    counter += 1
    ossz = ossz + be
    if legnagyobb < be:
        legnagyobb = be
    be = int(input("Mondj egy másikat: "))
print(f"{counter} számot adtál meg, {ossz/counter} az átlaguk, a legnagyobb pedig {legnagyobb} volt.")