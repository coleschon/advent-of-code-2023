import sys
sys.path.append('/Users/cperschon/sources-external/advent-of-code-2023/')

from utils import split_lists, intify

filename = "ex.txt"

# ---------------------------------------- HELPERS ----------------------------------------
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
    return file[-1] + file_prediction(diffs)
# -----------------------------------------------------------------------------------------

sums = 0
lists = split_lists(filename)
for list in lists:
    list = intify(list)
    print(file_prediction(list))
    sums += file_prediction(list)

print(sums)
