# { ...
#   cout >> "N nél nem nagyobb páratlan számoknak összege";
#   return 0;
# }

be = int(input("Melyik számnál kisebb páratlan számoknak összegét szeretnéd látni: "))
ossz = 0
for i in range(1, be, 2):
    ossz = ossz + i
print(ossz)