def tree(x: int, y: int, memo={}) -> int:
    if x == 0 or y == 0:
        return 1
    else:
        if (x,y) in memo:
            return memo[(x, y)]
        else:

            memo[(x, y)] = tree(x-1, y, memo) + tree(x, y-1, memo)
            return memo[(x, y)]

print(tree(20, 20))
