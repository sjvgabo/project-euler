"""
Nth Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import time


def prime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False

    return True


def nth_prime(digit):
    nth = 1
    temp = 2
    prime_number = 2
    while nth != digit:
        temp += 1
        if prime(temp):
            nth += 1
            prime_number = temp

    return prime_number


start = time.time()
print(nth_prime(10001))
end = time.time()

print(end-start)
