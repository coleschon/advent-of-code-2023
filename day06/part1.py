filename = "input.txt"

def get_list(starter):
    list = []
    start = 0
    with open(filename) as file:
        lines = file.readlines()
    with open(filename) as file:
        for line in file:
            word = ""
            for i in range(0, len(line)):
                elm = line[i]
                word += elm
                if (word == starter):
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
                    elif lastelmnum:   
                        list.append(int(num))
                        lastelmnum = False
                        num = ""
                return list
    return list

times = get_list("Time:")
distances = get_list("Distance:")

wins = [0]*len(times)
for i in range(0, len(times)):
    time = times[i]
    best_dist = distances[i]
    speed = -1
    for charge in range(0, time+1):
        speed += 1
        dist = 0
        steps = []
        print(speed)
        for step in range(charge+1, time+1):
            steps.append(step)
            dist += speed
        if dist > best_dist:
            wins[i] += 1
print("wins: " + str(wins))
total = 1
for win in wins:
    total *= win
print(total)
