filename = "input.txt"

# ---------------------------------------- HELPERS ----------------------------------------

def line_to_list(prefix):
    list = []
    start = 0
    with open(filename) as file:
        lines = len(file.readlines())
    with open(filename) as file:
        for line in file:
            lines -= 1
            word = ""
            for i in range(0, len(line)):
                elm = line[i]
                word += elm
                if (word == prefix):
                    start = i+1
                    break
            if start != 0:
                lastelmnum = False
                num = ""
                for i in range(0, len(line)):
                    elm = line[i]
                    if elm.isnumeric():
                        num += elm
                        lastelmnum = True
                    if (not elm.isnumeric() and lastelmnum) or (i == len(line)-1 and lines == 0):
                        list.append(int(num))
                        lastelmnum = False
                        num = ""
                return list
    return list

def concatenate_list(list):
    result = ""
    for elm in list:
        result += str(elm)
    return result

def list_to_string(prefix):
    return concatenate_list(line_to_list(prefix))

# -----------------------------------------------------------------------------------------

times = []
times.append(int(list_to_string("Time:")))
distances = []
distances.append(int(list_to_string("Distance:")))

wins = [0]*len(times)
for i in range(0, len(times)):
    time = times[i]
    best_dist = distances[i]
    speed = -1
    winning = False
    for charge in range(0, time+1):
        speed += 1
        dist = speed * (time - charge)
        if dist > best_dist:
            wins[i] += 1
            winning = True
        # bail out when we know no other runs will win
        elif winning:
            break
total = 1
for win in wins:
    total *= win
print(total)
