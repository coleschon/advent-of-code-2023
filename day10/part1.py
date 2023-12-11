import sys

# Append utils path
sys.path.append('/Users/cperschon/sources-external/advent-of-code-2023/')

from utils import *

filename = sys.argv[1]

# ---------------------------------------- HELPERS ----------------------------------------
class Pos:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self): # str() implementation
        return "({} , {})".format(self.row, self.col)

    def __repr__(self):
        return "({} , {})".format(self.row, self.col)
    
    def __eq__(self, other): # == operator
        return self.row == other.row and self.col == other.col
    
    def __ne__(self, other): # != operator
        return not (self == other)

def get_s(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] == 'S':
                return Pos(i, j)
    return Pos(-1, -1)

def get_next_pipe(pos, mat, seen):
    rows = len(mat)
    cols = len(mat[0])
    up = Pos(pos.row-1, pos.col)
    down = Pos(pos.row+1, pos.col)
    left = Pos(pos.row, pos.col-1)
    right = Pos(pos.row, pos.col+1)

    pipe = mat[pos.row][pos.col]
    if pipe == 'S':
        if pos.row-1 >= 0 and (mat[pos.row-1][pos.col] == '|' or mat[pos.row-1][pos.col] == '7' or mat[pos.row-1][pos.col] == 'F'):
            if up not in seen: return up # up
        if pos.row+1 < rows and (mat[pos.row+1][pos.col] == '|' or mat[pos.row+1][pos.col] == 'L' or mat[pos.row+1][pos.col] == 'J'):
            if down not in seen: return down # down
        if pos.col-1 >= 0 and (mat[pos.row][pos.col-1] == '-' or mat[pos.row][pos.col-1] == 'L' or mat[pos.row][pos.col-1] == 'F'):
            if left not in seen: return left # left
        if pos.col+1 < cols and (mat[pos.row][pos.col+1] == '-' or mat[pos.row][pos.col+1] == '7' or mat[pos.row][pos.col+1] == 'J'):
            if right not in seen: return right # right
    elif pipe == '|':
        if pos.row-1 >= 0 and up not in seen: return up  # up
        if pos.row+1 < rows and down not in seen: return down  # down
    elif pipe == '-':
        if pos.col-1 >= 0 and left not in seen: return left  # left
        if pos.col+1 < cols and right not in seen: return right  # right
    elif pipe == 'L':
        if pos.row-1 >= 0 and up not in seen: return up  # up
        if pos.col+1 < cols and right not in seen: return right  # right
    elif pipe == 'J':
        if pos.row-1 >= 0 and up not in seen: return up  # up
        if pos.col-1 >= 0 and left not in seen: return left  # left
    elif pipe == '7':
        if pos.row+1 < rows and down not in seen: return down  # down
        if pos.col-1 >= 0 and left not in seen: return left  # left
    elif pipe == 'F':
        if pos.row+1 < rows and down not in seen: return down  # down
        if pos.col+1 < cols and right not in seen: return right  # right

    return Pos(-1, -1)
    
# -----------------------------------------------------------------------------------------

mat = get_mat(filename)

seen = []
count = 0
cur = get_s(mat)
while True:
    if cur.row == -1 and cur.col == -1: break
    # print("{} = {}".format(cur, mat[cur.row][cur.col]))
    seen.append(cur)
    cur = get_next_pipe(cur, mat, seen)
    count += 1
    

# print_mat(mat)
print(int(count / 2))