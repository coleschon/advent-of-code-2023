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

def expand(mat):

    rows = len(mat)
    cols = len(mat[0])

    empty_rows = []
    for row in range(0, rows):
        count = 0
        for col in range(0, cols):
            if mat[row][col] != '.':
                break
            count += 1
        if count == cols: empty_rows.append(row)
    # print(empty_rows)

    extra = 0
    for empty in empty_rows:
        mat.insert(empty + extra, ['.'] * cols)
        extra += 1
        rows += 1

    empty_cols = []
    for col in range(0, cols):
        count = 0
        for row in range(0, rows):
            if mat[row][col] != '.':
                break
            count += 1
        if count == rows: empty_cols.append(col) 
    # print(empty_cols)

    extra = 0
    for empty in empty_cols:
        for row in range(0, rows):
            mat[row].insert(empty + extra, '.')
        extra += 1
    # print(cols)  

def get_galaxies(mat):
    rows = len(mat)
    cols = len(mat[0])

    galaxies = []
    for row in range(0, rows):
        for col in range(0, cols):
            if mat[row][col] == '#':
                galaxies.append(Pos(row, col))
    
    return galaxies

def is_valid(pos, mat, visited):
    rows = len(mat)
    cols = len(mat[0])

    # If cell lies out of bounds
    if (pos.row < 0 or pos.col < 0 or pos.row >= rows or pos.col >= cols): return False

    # If cell is already visited
    # for row in visi

    if visited[pos.row][pos.col]:
        return False
 
    # Otherwise
    return True

def closest_neighbor_dist(galaxy, mat):
    rows = len(mat)
    cols = len(mat[0])
    queue = []
    queue.append(galaxy)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distance = [[0 for _ in range(cols)] for _ in range(rows)]
    # visited[galaxy.row][galaxy.col] = True
    
    paths = []
    while len(queue) > 0:
        # print(queue)
        pos = queue.pop(0)

        if mat[pos.row][pos.col] == '#' and visited[pos.row][pos.col]: paths.append(distance[pos.row][pos.col])
        visited[pos.row][pos.col] = True

        up = Pos(pos.row-1, pos.col)
        down = Pos(pos.row+1, pos.col)
        left = Pos(pos.row, pos.col-1)
        right = Pos(pos.row, pos.col+1)
        
        if is_valid(up, mat, visited):
            queue.append(up)
            visited[pos.row-1][pos.col] = True
            distance[pos.row-1][pos.col] = distance[pos.row][pos.col]+1
        if is_valid(down, mat, visited):
            queue.append(down)
            visited[pos.row+1][pos.col] = True
            distance[pos.row+1][pos.col] = distance[pos.row][pos.col]+1
        if is_valid(left, mat, visited):
            queue.append(left)
            visited[pos.row][pos.col-1] = True
            distance[pos.row][pos.col-1] = distance[pos.row][pos.col]+1
        if is_valid(right, mat, visited):
            queue.append(right)
            visited[pos.row][pos.col+1] = True
            distance[pos.row][pos.col+1] = distance[pos.row][pos.col]+1
    
    return paths

# -----------------------------------------------------------------------------------------

mat = get_mat(filename)
print_mat(mat)
expand(mat)
print()
print_mat(mat)

tot = 0
galaxies = get_galaxies(mat)
for galaxy in galaxies:
    closest = closest_neighbor_dist(galaxy, mat)
    mat[galaxy.row][galaxy.col] = 'x'

    print(closest)
    tot += sum(closest)
    # break

print(tot)