"""
My method uses brute force which can be fast enough for small to fairly large numbers
But the best solution is using the correct formula for getting the sum of square
And the square of sums

Square of sums = n^2 * (n+1)^2 * 1/4
Sum of squares = n * (n+1) * (2n+1) * 1/6
"""
import time


def sum_square(num):
    return sum([number**2 for number in range(1, num+1)])


def square_sum(num):
    return (sum([number for number in range(1, num+1)]))**2


# my solution
def sum_square_difference(num):
    return square_sum(num) - sum_square(num)


# best solution
def sum_square_difference2(num):
    sum_sq = num*(num-1)/2
    sq_sum = (2*num - 1)*(num+1)*num/6

    return sum_sq**2 - sq_sum


start = time.time()
print(sum_square_difference(100000000))
end = time.time()

print(f'sam: {start - end}')

start = time.time()
print(sum_square_difference2(100000000))
end = time.time()

print(f'euler: {start - end}')
