
filename = "day3-input.txt"

def isnum(elm):
    
    return elm == "0" or elm == "1" or elm == "2" or elm == "3" or elm == "4" or elm == "5" or elm == "6" or elm == "7" or elm == "8" or elm == "9"

def issymbol(elm):
    return (not isnum(elm)) and elm != '.' and elm != '\n' and elm != ''

def build_matrix(filename):
    cols = 0
    rows = 0
    with open(filename) as file:
        cols, rows = (len(file.readline()), len(file.readlines())+1)
        matrix = [[""]*cols]*rows
    with open(filename) as file:
        r = 0
        for line in file:
            lined = [""]*cols
            for c in range(0, len(line)):
                lined[c] = line[c]
            matrix[r] = lined
            r += 1
    return matrix

def get_neighbors(matrix, row, col):
    row_len = len(matrix)
    col_len = len(matrix[0])
    neighbors = []
    # top left
    if (row-1 >= 0 and col-1 >= 0):
        neighbors.append(matrix[row-1][col-1])
    
    
    # top
    if (row-1 >= 0):
        neighbors.append(matrix[row-1][col])
    # top right 
    if (row-1 >= 0 and col+1 < col_len):
        neighbors.append(matrix[row-1][col+1])
    # right
    if (col+1 < col_len):
        neighbors.append(matrix[row][col+1])
    # bottom right
    if (row+1 < row_len and col+1 < col_len):
        neighbors.append(matrix[row+1][col+1])
    # bottom
    if (row+1 < row_len):
        neighbors.append(matrix[row+1][col])
    # bottom left
    if (row+1 < row_len and col-1 >= 0):
        neighbors.append(matrix[row+1][col-1])
    # left
    if (col-1 >= 0):
        neighbors.append(matrix[row][col-1])
    return neighbors

sum = 0
matrix = build_matrix(filename)
cols = 0
rows = 0
with open(filename) as file:
    cols, rows = (len(file.readline()), len(file.readlines())+1)
with open(filename) as file:
    for r in range (0, rows):
        num = ""
        lastelmnum = False
        valid = False
        for c in range(0, cols):
            elm = matrix[r][c]
            if isnum(elm):
                num += elm
                lastelmnum = True
                if not valid:
                    for neighbors in get_neighbors(matrix, r, c):
                        if issymbol(neighbors):
                            valid = True
                            break
            elif lastelmnum:
                if valid:


                    num = int(num)
                    sum += num
                num = ""
                lastelmnum = False
                valid = False


print(sum)




