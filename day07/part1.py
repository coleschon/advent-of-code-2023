from ordered_enum import OrderedEnum



filename = "input.txt"




# ---------------------------------------- HELPERS ----------------------------------------
class Type(OrderedEnum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

class Card:
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T" ,"J", "Q", "K", "A"]


    def __init__(self, val):


        self.value = str(val)

    def __eq__(self, other): # == operator
        return self.value == other.value

    def __ne__(self, other): # != operator
        return not (self == other)

    def __lt__(self, other): # < operator
        return self.values.index(self.value) < self.values.index(other.value)

    def __le__(self, other): # <= operator
        return self == other or self < other

    def __gt__(self, other): # > operator
        return self.values.index(self.value) > self.values.index(other.value)

    def __ge__(self, other): # >= operator
        return self == other or self > other

    def __str__(self): # str() implementation
        return "{}".format(self.value)
    
    def __repr__(self):
        return "{}".format(self.value)

class Hand:
    def __init__(self, cards, bet):
        self.bet = int(bet)
        self.true_cards = cards.copy()
        cards.sort(reverse=True)
        self.cards = cards
        self.type = self.get_type()
        self.get_type_cards()

    def get_type(self):
        # Five of a kind
        if self.cards[0] == self.cards[1] == self.cards[2] == self.cards[3] == self.cards[4]:
            return Type.FIVE_OF_A_KIND
        # Four of a kind
        for i in range(0, 2):
            card1 = self.cards[i]
            count = 0
            for j in range(i+1, len(self.cards)):
                card2 = self.cards[j]
                if card1 == card2:
                    count += 1
                    if count == 3:
                        return Type.FOUR_OF_A_KIND
        # Full house
        if (self.cards[0] == self.cards[1] == self.cards[2] and self.cards[3] == self.cards[4]) or (self.cards[0] == self.cards[1] and self.cards[2] == self.cards[3] == self.cards[4]):
            return Type.FULL_HOUSE
        # Three of a kind
        for i in range(0, 3):
            card1 = self.cards[i]
            count = 0
            for j in range(i+1, len(self.cards)):
                card2 = self.cards[j]
                if card1 == card2:
                    count += 1
                    if count == 2:
                        return Type.THREE_OF_A_KIND
        # Two pair
        while (True):        
            break_index = 0
            pairs = 0
            for i in range(0, 4):
                card1 = self.cards[i]
                for j in range(i+1, len(self.cards)):
                    card2 = self.cards[j]
                    if card1 == card2:
                        break_index = j
                        pairs += 1
            for i in range(break_index, 4):
                card1 = self.cards[i]
                for j in range(i+1, len(self.cards)):
                    card2 = self.cards[j]
                    if card1 == card2:
                        pairs += 1
            if pairs == 2:
                return Type.TWO_PAIR
            break                
        # One pair
        for i in range(0, 4):
            if self.cards[i] == self.cards[i+1]:
                return Type.ONE_PAIR
        # High card
        return Type.HIGH_CARD

    def get_type_cards(self):
         # Five of a kind
        if self.type is Type.FIVE_OF_A_KIND:
            self.type_cards = self.cards
        # Four of a kind
        elif self.type is Type.FOUR_OF_A_KIND:
            if self.cards[0] == self.cards[1] and self.cards[0] > self.cards[4]:
                self.type_cards = self.cards
            else:
                self.type_cards = [self.cards[4]]*4
                self.type_cards.append(self.cards[0])
        # Full house
        elif self.type is Type.FULL_HOUSE:
            self.type_cards = [self.cards[2]]*3
            for card in self.cards:
                if card != self.cards[2]:
                    self.type_cards.append(card)
        # Three of a kind
        elif self.type is Type.THREE_OF_A_KIND:
            for i in range(0, 3):
                card1 = self.cards[i]
                count = 0
                three_card = Card("1")
                for j in range(i+1, len(self.cards)):
                    card2 = self.cards[j]
                    if card1 == card2:
                        count += 1
                        if count == 2:
                            self.type_cards = [card1]*3
                            three_card = card1
                            for card in self.cards:
                                if card != three_card:
                                    self.type_cards.append(card)
                            break
        # Two pair
        elif self.type is Type.TWO_PAIR:
            pairs = []
            for i in range(0, 4):
                if self.cards[i] == self.cards[i+1]:
                    pairs.append(self.cards[i])
                    i += 1
            pairs.sort(reverse=True) # is this sorted correctly?
            self.type_cards = []
            for card in pairs:
                self.type_cards.append(card)
                self.type_cards.append(card)
            for card in self.cards:
                if card not in pairs:
                    self.type_cards.append(card)
        # One pair
        elif self.type is Type.ONE_PAIR:
            one_card = Card("1") 
            for i in range(0, 4):
                if self.cards[i] == self.cards[i+1]:
                    self.type_cards = [self.cards[i]]*2
                    one_card = self.cards[i]



                    i += 1
            for card in self.cards:
                if card != one_card:
                    self.type_cards.append(card)
        # High card
        elif self.type is Type.HIGH_CARD:
            self.type_cards = self.cards

    def __eq__(self, other): # == operator
        return self.type == other.type and self.true_cards == other.true_cards

    def __ne__(self, other): # != operator
        return not (self == other)

    def __lt__(self, other): # < operator
        if self.type == other.type:
            # print(self)
            # print(other)
            for i in range(0, 5):
                if self.true_cards[i] != other.true_cards[i]:
                    return self.true_cards[i] > other.true_cards[i]
        return self.type < other.type

    def __le__(self, other): # <= operator
        return self == other or self < other

    def __gt__(self, other): # > operator
        if self.type == other.type:
            for i in range(0, 5):
                if self.true_cards[i] != other.true_cards[i]:
                    return self.true_cards[i] < other.true_cards[i]
        return self.type > other.type
    
    def __ge__(self, other): # >= operator
        return self == other or self > other

    def __str__(self): # str() implementation
        return "{} {}".format(self.type, self.true_cards)

    def __repr__(self):
        return "{} {}".format(self.type, self.true_cards)

def split_lists():
    lists = []
    with open(filename) as file:
        for line in file:
            lists.append(line.split())
    return lists

def concatenate_list(list):
    result = ""
    for elm in list:
        result += str(elm)
    return result

def list_to_string(prefix):
    return concatenate_list(line_to_list(prefix))

# -----------------------------------------------------------------------------------------

lines = 0
with open(filename) as file:
    lines += len(file.readlines())

# lists = [[""]*2]*lin
# es
lists = split_lists()
hands = []
for entry in lists:
    cards = []
    for i in range(0, len(entry[0])):
        cards.append(Card(entry[0][i]))
    hands.append(Hand(cards, entry[1]))


# for hand in hands:
#     print(hand)

hands.sort(reverse=True)
sum = 0

scalar = 1
for hand in hands:
    # print(str(scalar) + ". ", hand)
    # print(hand)

    sum += scalar * hand.bet
    scalar += 1
print(sum)
