def read(filename):
    """
    Reads a file and returns a list of names that is sorted alphabetically

    """
    with open(filename) as read_line:
        name_set = read_line.readline()
        name_set = name_set.strip('"').split('","')
        name_set.sort()

    return name_set


def get_score(text):
    score = 0
    name_dict = [1,'a','b','c','d','e','f','g','h','i','j','k'\
        ,'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in text.lower():
        score += name_dict.index(char)

    return score


def evaluate_sum(name_list):
    name_list = read(name_list)
    scores = 0
    i = 1
    for name in name_list:
        scores += get_score(name) * i
        i += 1

    return scores


print(evaluate_sum('p022_names.txt'))