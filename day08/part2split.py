
filename = "example3.txt"

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

def get_starting_nodes(nodes):
    starting_nodes = []
    for key in nodes.keys():
        node = nodes[key]
        if node.value[2] == 'A':
            starting_nodes.append(node)
    return starting_nodes

def all_nodes_finished(nodes):
    for node in nodes:
        if node.value[2] != 'Z':
            return False
    return True
# -----------------------------------------------------------------------------------------

nodes = {}
head = None
lists = split_lists()
directions = lists[0][0]
# print(directions)
for i in range(2, len(lists)):
    line = lists[i]
    node = Node(line[0], line[2].strip("(,)"), line[3].strip("(,)"))
    nodes[node.value] = node

i = 0
cycles = []
starting_nodes = get_starting_nodes(nodes)
for current in starting_nodes:
    start = current
    cycle = []
    while True:
        cycle.append(current)
        dir = directions[i]
        if dir == 'L': current = nodes[current.left]
        else: current = nodes[current.right]
        i = i+1 if i < len(directions)-1 else 0
        if current == start: break
    cycles.add(cycle)

for cycle in cycles:
    print(cycle)



# i = 0
# steps = 0
# while not all_nodes_finished(current_nodes):
#     print()
#     for node in current_nodes:
#         print(node)
#     dir = directions[i]
#     steps += 1
#     for j in range(0, len(current_nodes)):
#         current = current_nodes[j]
#         if dir == 'L': current = nodes[current.left]
#         else: current = nodes[current.right]
#         current_nodes[j] = current
#     i = i+1 if i < len(directions)-1 else 0

# print(steps)
