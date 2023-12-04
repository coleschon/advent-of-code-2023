sum = 0

def isnum(elm):
    return elm == "0" or elm == "1" or elm == "2" or elm == "3" or elm == "4" or elm == "5" or elm == "6" or elm == "7" or elm == "8" or elm == "9"

def num(str):
    if "zero" in str.lower():
        return "0"
    if "one" in str.lower():
        return "1"
    if "two" in str.lower():
        return "2"
    if "three" in str.lower():
        return "3"
    if "four" in str.lower():
        return "4"
    if "five" in str.lower():
        return "5"
    if "six" in str.lower():
        return "6"
    if "seven" in str.lower():
        return "7"
    if "eight" in str.lower():
        return "8"
    if "nine" in str.lower():
        return "9"
    return ""

with open("p1.txt") as file:
    for line in file:
        first = ""
        last = ""

        sofar = ""
        for elm in line:
            if isnum(elm):
                first = elm
                break
            sofar += elm
            if num(sofar) != "":
                first = num(sofar)
                break
        sofar = ""
        for elm in reversed(line):
            if isnum(elm):
                last = elm
                break
            sofar = elm + sofar
            if num(sofar) != "":
                last = num(sofar)
                break
        # print(first)
        
        d = int(first + last)
        sum += int(first + last)

print(sum)


