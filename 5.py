# Fibonacci number

be = int(input("Hanyadik fibonacci számot szeretnéd: "))
f0 = 0
f1 = 1
fn = f0 + f1
for i in range(0, be-1):
    fn = f1 + f0
    f0 = f1
    f1 = fn
    print(fn)