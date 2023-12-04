filename = "example.txt"

def isnum(elm):
    return elm == "0" or elm == "1" or elm == "2" or elm == "3" or elm == "4" or elm == "5" or elm == "6" or elm == "7" or elm == "8" or elm == "9"

sum = 0
card_counts = []
with open(filename) as file:
    card_counts = [1]*(len(file.readlines()))
with open(filename) as file:
    for line in file:
        winners = []
        numbers = []
        start = 0
        lastelmnum = False
        count = ""
        switch = False
        card = ""
        while line[start] != ":":
            if line[start].isdigit(): card += line[start]
            start += 1
        card = int(card)
        card -= 1

        for i in range(start, len(line)):
            elm = line[i]
            if elm.isdigit():
                count += elm
                lastelmnum = True
            elif lastelmnum:
                if switch: numbers.append(count)
                else: winners.append(count)
                count = ""
                lastelmnum = False
            if elm == '|':
                switch = True
        score = 0


        next_card = card+1
        for num in numbers:
            if num in winners:
                if next_card < len(card_counts):
                    for i in range(0, card_counts[card]):
                        card_counts[next_card] +=1
                    next_card +=1

for count in card_counts:
    sum += count
print(sum)
