import time


def largest_prime(num):

    if num < 2:
        return

    x = 2
    largest = num
    max_factor = num**0.5

    while largest % 2 == 0:
        largest /= 2

    x = 3
    while largest > 1 and x < max_factor:
        # x if is a factor
        if largest % x == 0:
            largest /= x
            max_factor = largest ** 0.5
        x += 2

    return int(largest)


x = time.time()
print(x)
print(largest_prime(1000000000877878787))
y = time.time()

print(y-x)
