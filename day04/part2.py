filename = "example.txt"


card_counts = []
with open(filename) as file:
    card_counts = [1]*(len(file.readlines()))

sum = 0
with open(filename) as file:
    for line in file:
        # get card number
        card = ""
        start = 0
        while line[start] != ":":
            if line[start].isdigit():
                card += line[start]
            start += 1
        card = int(card)-1

        # count card winners
        lastelmnum = False
        switch = False
        winners = []
        numbers = []
        count = ""
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
        
        # count card copies
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
