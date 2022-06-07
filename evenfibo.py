def even_fibo():
    x = 0
    y = 1

    sum = 0
    while x+y < 4000000:
        x, y = x+y, x

        if x % 2 == 0:
            sum += x

    return sum

print(even_fibo())
