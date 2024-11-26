# első száz páros szám összege
n = 200
ossz = 0
counter = 0
for i in range(1, n+1):
    if i % 2 == 0:
        ossz = ossz + i
        counter += 1
        print(i, counter)
print(ossz)