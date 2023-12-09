def split_lists(filename):
    lists = []
    with open(filename) as file:
        for line in file:
            lists.append(line.split())
    return lists

def intify(list):
    # return list(map(int, list))
    return [int(i) for i in list]