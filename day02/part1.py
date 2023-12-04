def isnum(elm):
    return elm == "0" or elm == "1" or elm == "2" or elm == "3" or elm == "4" or elm == "5" or elm == "6" or elm == "7" or elm == "8" or elm == "9"

red_max = 12
green_max = 13
blue_max = 14

def check_color(str, count):
    if "red" in str:
        # print("", count, " red cubes > ", red_max, " red cubes?")
        if count > red_max: return -1
        else: return 0
    if "green" in str:
        # print("", count, " green cubes > ", green_max, " green cubes?")
        if count > green_max: return -1
        else: return 0
    if "blue" in str:
        # print("", count, " blue cubes > ", blue_max, " blue cubes?")
        if count > blue_max: return -1
        else: return 0
    return 1

with open("day2_input.txt") as file:
    ids = 0
    lastid = 0
    for line in file:
        start = 0
        game = ""
        while line[start] != ":":
            if isnum(line[start]): game += line[start]
            start += 1
        game = int(game)
        lastid = game

        count = ""
        color = ""
        lastelmnum = False
        for i in range(start, len(line)):
            elm = line[i]
            if isnum(elm):
                count += elm
                lastelmnum = True
            elif lastelmnum:
                count = int(count)
                lastelmnum = False
            elif '\n' in elm:
                ids += game
            else:
                color += elm
                check = check_color(color, count)
                if check == -1: 
                    lastid = 0
                    break
                if check == 0:
                    count = ""
                    color = ""
    ids += lastid
    print(ids)
        