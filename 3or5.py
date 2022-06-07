def sum_of_3_and_5(num):
    """
    gets the sum of all digits that are multiples of 3 or 5
    """
    return sum([dig for dig in range(1,num) if dig % 3 == 0 or dig % 5 == 0])


print(sum_of_3_and_5(1000))

