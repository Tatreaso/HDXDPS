# bekér szám, print osztói

be = int(input("Mondj egy számot melynek keresed osztóit: "))
for i in range(1, be+1):
    if be % i == 0:
        print(i)