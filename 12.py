# ki irja n-ig a primeket

N = int(input("Adj meg egy szamot: "))
for szam in range(2, N + 1):
    prim = True
    for oszto in range(2, szam):
        if szam % oszto == 0:
            prim = False
            break
    if prim:
        print(szam)