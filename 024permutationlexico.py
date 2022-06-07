digits = [1, 2, 0,3,4,5,6,7,8,9]


def permutations(digits: list):
    if len(digits) == 0:
        return []

    if len(digits) == 1:
        return [digits]

    else:
        l = []
        for i in range(len(digits)):
            m = digits[i]
            remaining = digits[:i] + digits[i+1:]
            for p in permutations(remaining):
                l.append([m]+p)
        return l


def get_sorted_permutations(digits):
    perms =permutations(digits)
    perms.sort()
    return perms


perms = get_sorted_permutations(digits)
print(perms[999999])

