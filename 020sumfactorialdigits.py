def factorial(num):
    if num == 1:
        return num
    else:
        return num * (factorial(num-1))


def sum_factorial(num):
    digit = factorial(num)
    total = 0
    for char in str(digit):
        total += int(char)

    return total


print(sum_factorial(100))
