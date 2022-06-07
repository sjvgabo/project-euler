



def map_num(num):
    num_map = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3,
               7: 5, 8: 5, 9: 4}
    tens_map = {1: 3, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
    teens_map = {0: 3, 1: 6, 2: 6, 3: 8, 4: 8, 5: 7, 6: 7, 7: 9, 8: 8, 9: 8}
    count = 0
    num = str(num)
    for i in range(len(num)):
        if num[i] == '0':
            continue
        if i != len(num)-2:
            count += num_map[int(num[i])]
        else:
            if num[i] == '1':
                count += teens_map[int(num[i+1])]
                break
            else:
                count += tens_map[int(num[i])]

    if len(num) == 3:
        count += 7
        if num[2] != '0' or num[1] != '0':
            count += 3
    if len(num) == 4:
        count += 8

    return count


total = 0
for j in range(1,1000+1):
    total += map_num(j)

print(total)


for j in range(1,100):
    print(f'{j}: {map_num(j)}')

