def get_divisors(num):
    divisors = []
    for i in range(1, num//2+1):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors)


def get_abundant_nums(limit):
    abundant_nums = []
    for i in range(2, limit):
        if get_divisors(i) > i:
            abundant_nums.append(i)

    return abundant_nums


def get_all_non_abundant_nums_perms(abund_nums):
    perms = {}
    abund_perms = set()
    non_abund_perms = []
    for x in abund_nums:
        for y in abund_nums:
            if (x,y) in perms:
                continue
            else:
                if x + y < 28123:
                    perms[(x, y)] = x+y
                    abund_perms.add(x+y)

    for i in range(1, 28123):
        if i not in abund_perms:
            non_abund_perms.append(i)

    return (non_abund_perms)


abund_nums = get_abundant_nums(28123)
print(sum(get_all_non_abundant_nums_perms(abund_nums)))

