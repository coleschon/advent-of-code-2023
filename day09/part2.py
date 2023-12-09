
filename = "in.txt"

# ---------------------------------------- HELPERS ----------------------------------------
def split_lists():
    lists = []
    with open(filename) as file:
        for line in file:
            lists.append(line.split())
    return lists

def inty(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])
    return list

def all_zero(list):
    for elm in list:
        if elm != 0:
            return False
    return True

def file_prediction(file):
    if all_zero(file):
        return 0
    diffs = []
    for i in range(0, len(file)-1):
        diffs.append(file[i+1] - file[i])
    return file[0] - file_prediction(diffs)
# -----------------------------------------------------------------------------------------

sums = 0
lists = split_lists()
for list in lists:
    list = inty(list)
    print(file_prediction(list))
    sums += file_prediction(list)

print(sums)
