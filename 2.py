# első valahány(N) négyzetszám

be = int(input("Add meg meddig szeretnéd a négyzetszámokat: "))
jelenlegi = 1
for i in range(1, be+1):
    jelenlegi = i**2
    print(jelenlegi)