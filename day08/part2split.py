
from itertools import cycle
from math import lcm

filename = "input.txt"

# ---------------------------------------- HELPERS ----------------------------------------
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.dir = None

    def __init__(self, value, left, right ):
        self.value = value
        self.left = left
        self.right = right
        self.dir = None
    
    def __eq__(self, other): # == operator
        return self.value == other.value and self.left == other.left and self.right == other.right and self.dir == other.dir
    
    def __ne__(self, other): # != operator
        return not (self == other)
    
    def __str__(self): # str() implementation
        return "{} --> ({}, {}, {})".format(self.value, self.left, self.right, self.dir)

    def __repr__(self):
        return "{} --> ({}, {}, {})".format(self.value, self.left, self.right, self.dir)
    
    def set_dir(self, i):
        self.dir = i

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

def get_pos(list, elm):
    for i in range(0, len(list)):
        if list[i] == elm:
            return i
    return -1

def lcm_of_array(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        num1 = lcm
        num2 = arr[i]
        gcd = 1
        # Finding GCD using Euclidean algorithm
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        gcd = num1
        lcm = (lcm * arr[i]) // gcd
    return lcm
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

starting_nodes = get_starting_nodes(nodes)
lens = []
for current in starting_nodes:
    plen = 0
    i = 0
    while current.value[-1] != 'Z':
        dir = directions[i]
        if dir == 'L': current = nodes[current.left]
        else: current = nodes[current.right]
        i = i+1 if i < len(directions)-1 else 0
        plen += 1
    lens.append(plen)


print(lcm(*lens))

# all_seen_nodes = []
# all_starting_steps = []
# all_starting_pos = []
# all_starting_dir = []
# starting_nodes = get_starting_nodes(nodes)
# for current in starting_nodes:
#     seen_nodes = []
#     i = 0
#     steps = 0
#     pos = 0
#     while True:
#         # print("begin: ", seen_nodes)
#         pos = get_pos(seen_nodes, current)
#         if pos > -1: break

#         current.set_dir(i)
#         seen_nodes.append(current)
#         dir = directions[i]
#         if dir == 'L': current = nodes[current.left]
#         else: current = nodes[current.right]
#         i = i+1 if i < len(directions)-1 else 0
#         steps += 1
#         # print("end: ", seen_nodes)

#     cycle = []
#     for i in range(pos, len(seen_nodes)):
#         cycle.append(seen_nodes[i])
#     all_seen_nodes.append(cycle)
#     all_starting_pos.append(pos)
#     all_starting_dir.append(i)
#     all_starting_steps.append(steps)

#     for seen in seen_nodes:
#         print(seen)
#     print()



# lens = []
# for i in range(0, len(all_seen_nodes)):
#     seen = all_seen_nodes[i]
#     pos = all_starting_pos[i]
#     dir = all_starting_dir[i]
#     steps = all_starting_steps[i]
#     print("steps - ", steps)
#     print("pos --- ", pos)
#     print("dir i - ", dir)
#     lens.append(len(seen))
#     for node in seen:
#         print(node)
#     print()


# print(lcm_of_array(lens))

# print()
# for elm in cycle:
#     print(elm)

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
