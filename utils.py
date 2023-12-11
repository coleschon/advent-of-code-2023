def split_lists(filename):
    lists = []
    with open(filename) as file:
        for line in file:
            lists.append(line.split())
    return lists

def get_mat(filename):
    lists = []
    with open(filename) as file:
        for line in file:
            list = []
            for i in range (0, len(line)):
                if line[i] != '\n': list.append(line[i])
            lists.append(list)
    return lists

def print_mat(mat):
    for row in mat:
        print(row)

def intify(list):
    # return list(map(int, list))
    return [int(i) for i in list]