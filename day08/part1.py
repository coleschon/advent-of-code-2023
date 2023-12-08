
filename = "input.txt"

# ---------------------------------------- HELPERS ----------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __init__(self, value, left, right ):
        self.value = value
        self.left = left
        self.right = right
    
    def __eq__(self, other): # == operator
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __ne__(self, other): # != operator
        return not (self == other)
    
    def __str__(self): # str() implementation
        return "{} --> ({}, {})".format(self.value, self.left, self.right)

    def __repr__(self):
        return "{} --> ({}, {})".format(self.value, self.left, self.right)

def split_lists():
    lists = []
    with open(filename) as file:
        for line in file:
            lists.append(line.split())
    return lists
# -----------------------------------------------------------------------------------------

nodes = {}
head = None
lists = split_lists()
directions = lists[0][0]
print(directions)
for i in range(2, len(lists)):
    line = lists[i]
    node = Node(line[0], line[2].strip("(,)"), line[3].strip("(,)"))
    nodes[node.value] = node
    # print(node)
# print(lists)

i = 0
steps = 0
current = nodes['AAA']
while current.value != "ZZZ":
    dir = directions[i]
    steps += 1
    if dir == 'L':
        current = nodes[current.left]
    else:
        current = nodes[current.right]
    i = i+1 if i < len(directions)-1 else 0
print(steps)