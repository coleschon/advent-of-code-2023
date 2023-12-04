
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

def get_neighbor_positions(matrix, row, col):
    row_len = len(matrix)
    col_len = len(matrix[0])
    positions = []
    # top left
    if (row-1 >= 0 and col-1 >= 0):
        positions.append(Pos(row-1, col-1))
    # top
    if (row-1 >= 0):
        positions.append(Pos(row-1, col))
    # top right 
    if (row-1 >= 0 and col+1 < col_len):
        positions.append(Pos(row-1, col+1))
    # right
    if (col+1 < col_len):
        positions.append(Pos(row, col+1))
    # bottom right
    if (row+1 < row_len and col+1 < col_len):
        positions.append(Pos(row+1, col+1))
    # bottom
    if (row+1 < row_len):
        positions.append(Pos(row+1, col))
    # bottom left
    if (row+1 < row_len and col-1 >= 0):
        positions.append(Pos(row+1, col-1))
    # left
    if (col-1 >= 0):
        positions.append(Pos(row, col-1))
    return positions

class Number:
    def __init__(self, value, positions):
        self.value = value
        self.positions = positions

    def __eq__(self, other):
        if isinstance(other, Number):
            if self.value != other.value:
                return False
            for position in self.positions:
                if position not in other.positions:
                    return False
            for position in other.positions:
                if position not in self.positions:
                    return False
            return True
        return False

class Pos:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.row == other.row and self.col == other.col
        return False

sum = 0
numbers = []
matrix = build_matrix(filename)
cols = 0
rows = 0
with open(filename) as file:
    cols, rows = (len(file.readline()), len(file.readlines())+1)
with open(filename) as file:
    for r in range (0, rows):
        num = ""
        lastelmnum = False
        positions = []
        for c in range(0, cols):
            elm = matrix[r][c]
            if isnum(elm):
                num += elm
                lastelmnum = True
                positions.append(Pos(r, c))
            elif lastelmnum:
                number = Number(int(num), positions)
                numbers.append(number)
                num = ""
                lastelmnum = False
                positions = []
with open(filename) as file:
    for r in range (0, rows):
        num = ""
        lastelmnum = False
        positions = []
        for c in range(0, cols):
            elm = matrix[r][c]

            if elm == '*':
                gear_count = 0
                gear_ratio = 0
                used_positions = []
                neighbor_positions = get_neighbor_positions(matrix, r, c)
                for neighbor_position in neighbor_positions:
                    if neighbor_position not in used_positions:
                        # inefficent
                        for number in numbers:
                            if neighbor_position in number.positions:
                                if gear_count == 0:
                                    gear_ratio = 1
                                gear_ratio *= number.value
                                gear_count += 1

                                print(number.value)
                                for number_position in number.positions:
                                    used_positions.append(number_position)
                                break
                if gear_count > 1:    
                    sum += gear_ratio
                gear_ratio = 0
                used_positions = []
                print("new")
print(sum)






# for number in numbers:

#     print("value: ", number.value)
#     for pos in number.positions:
#         print("row: ", pos.row, " col: ", pos.col)
# print(numbers)




