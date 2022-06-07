import time


def collatz(limit):
    start = 13
    memo = {}
    biggest_chain = 0
    while start < limit:
        chain_length = 1
        n = start
        while n != 1:
            if n in memo:
                chain_length += memo[n]
                break
            if n % 2 == 0:
                n /= 2
                chain_length += 1
            else:
                n = (3*n + 1)/2
                chain_length += 2

        # once n is 1 or finds a memo

        memo[start] = chain_length
        if chain_length > biggest_chain:
            biggest_chain = chain_length
            biggest_start = start

        start += 1
    # print(memo)

    return biggest_start, biggest_chain


start = time.time()
collatz(1000000)
end = time.time()
print(end-start)