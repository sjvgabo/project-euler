def get_divisors(num):
    divisors = []
    for i in range(1, num//2+1):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors)


def get_amicable_numbers(limit):
    current = 1
    memo = {}
    amicables = set()
    while current < limit:
        for i in range(1, limit):
            if current in memo:
                current_divisors = memo[current]
            else:
                current_divisors = get_divisors(current)
                memo[current] = current_divisors
            if i in memo:
                compare_divisors = memo[i]
            else:
                compare_divisors = get_divisors(i)
                memo[i] = compare_divisors

            if current_divisors == i and current == compare_divisors and current != i:
                print(current)
                print(i)
                amicables.add(current)
                amicables.add(i)


        current += 1
    print(memo)
    return amicables


# print(get_amicable_numbers(10000))

print(sum({1184, 6368, 5564, 5020, 2924, 284, 6232, 1210, 220, 2620}))