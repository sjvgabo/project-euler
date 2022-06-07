def smallest_multiple(num):
    result = 1
    divisor = 2
    temp = result

    while divisor <= num:
        while result % divisor != 0:
            result += temp
        temp = result
        divisor += 1

    return result


print(smallest_multiple(9990))