# összeadós max 5000
n = 5000
ossz = 0
counter = 0
for i in range(1,5000):
    if ossz + i < 5000:
        ossz = ossz + i
        counter += 1
print(f"{counter} számot adtunk össze, {ossz} az összegük.")