def pyth_evaluate(a,b):
    return (a**2 + b**2)**1/2


def pyth_triplet():
    a = 1
    b = 1
    c = 1
    while a + b + c != 1000 or pyth_evaluate(a,b) != c**2:
        a += 3
        b += 4
        c += 9

        print(a, b, c)
    return a, b, c

print(pyth_triplet())


