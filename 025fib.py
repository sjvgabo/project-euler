# def fast_fib(n = None, memo = None):
#
#     if not n:
#         n = 1
#
#     if not memo:
#         memo = {}
#
#     if n in memo:
#         return memo[n]
#
#     if n == 1 or n == 2:
#         return 1
#
#     else:
#         memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
#         return memo[n]
#
def fib(n):
    x = 0
    y = 1
    index = 0
    while index != n:
        x, y = x+y, x
        index += 1

    return x


def index_1000_fib():
    x = 0
    y = 0
    while len(str(y)) < 1000:
        x += 1
        y = fib(x)
        if x % 10 == 0:
            print(x)
    return x


print(index_1000_fib())


