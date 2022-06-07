import math


def binary_search(lst, target):
    high = len(lst) - 1
    low = 0

    while low <= high:
        middle = (high + low) // 2
        print(f'low: {low} \nhigh: {high} \nmiddle: {middle}\n')
        if lst[middle] == target:
            return middle
        elif lst[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    print(f'low: {low} \nhigh: {high} \nmiddle: {middle}\n')
    return None


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(l, 100))
