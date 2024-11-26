# faktoriális

be = int(input("Add meg a faktoriálist! "))
ossz = 1
for i in range(1, be):
    ossz = ossz + i * ossz
print(ossz)