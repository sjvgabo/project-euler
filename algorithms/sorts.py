import time
import random


def bubble_sort(lst):
    counter = 0
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[-1 - j] < lst[-2 -j]:
                lst[-j - 1], lst[-j - 2] = lst[-2 - j], lst[-1 - j]
            counter += 1


def simple_sort(lst: list):
    lst_copy = lst[:]
    lst.clear()
    while lst_copy:
        index_of_biggest = 0

        if len(lst_copy) == 1:
            lst.append(lst_copy.pop())
        else:
            for i in range(1, len(lst_copy)):
                if lst_copy[i] < lst_copy[index_of_biggest]:
                    index_of_biggest = i

            lst.append(lst_copy.pop(index_of_biggest))


def selection_sort(lst):
    for i in range(len(lst)-1):
        smallest = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        if smallest != i:
            lst[i], lst[smallest] = lst[smallest], lst[i]


def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1


def merge(left, right):
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    middle = len(lst)//2
    left = lst[:middle]
    right = lst[middle:]

    return merge(merge_sort(left), merge_sort(right))


lst = [1,8, 4, 6, 3, 10, 9]
print(merge_sort(lst))

sort_methods = [merge_sort, 
           insertion_sort, 
           selection_sort, 
           simple_sort, 
           bubble_sort
          ]

def test_speed_all(sort_methods):
    for sort_method in sort_methods:
        lst = [random.randint(1, 10000) for _ in range(10000)]

        start = time.time()
        sort_method(lst)
        end = time.time()
        print(f'Sort Method: {sort_method.__name__}')
        print(f'Time: {end - start}')
    
