import time


def pal(text):
    return text == text[::-1]


def largest_palindrome(digit):

    x = int('9' * digit)
    y = int('9' * digit)
    largest = 0
    trial = x*y

    for i in range(x-10**(digit-1)):
        a = x - i

        for j in range(i, y+1):
            b = y - j
            trial = a*b
            if trial < largest:
                break
            if pal(str(trial)):
                if trial > largest:
                    largest = trial
    return largest


start = time.time()
print(largest_palindrome(5))
end = time.time()

print(end-start)

