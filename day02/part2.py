import sys


def isnum(elm):
    return elm == "0" or elm == "1" or elm == "2" or elm == "3" or elm == "4" or elm == "5" or elm == "6" or elm == "7" or elm == "8" or elm == "9"

def check_color(str, count):
    if "red" in str:
        print("", count, " red cubes < ", red_min, " red cubes?")
        if count < red_min: red_min = count
        return True
    if "green" in str:
        print("", count, " green cubes < ", green_min, " green cubes?")
        if count < green_min: green_min = count
        return True
    if "blue" in str:
        print("", count, " blue cubes < ", blue_min, " blue cubes?")
        if count < blue_min: blue_min = count
        return True
    return False


with open("day2_input.txt") as file:
    ids = 0
    
    lastid = 0

    sum = 0
    for line in file:
        red_min = 0
        green_min = 0
        blue_min = 0

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
                if "red" in color or "green" in color or "blue" in color:
                    if "red" in color:
                        print("", count, " red cubes < ", red_min, " red cubes?")
                        if count > red_min: red_min = count
                    elif "green" in color:
                        print("", count, " green cubes < ", green_min, " green cubes?")
                        if count > green_min: green_min = count
                    elif "blue" in color:
                        print("", count, " blue cubes < ", blue_min, " blue cubes?")
                        if count > blue_min: blue_min = count
                    count = ""
                    color = ""
        print("red: ", red_min, " blue: ", blue_min, " green: ", green_min)
        power = red_min * blue_min * green_min
        sum += power
    print(sum)
        