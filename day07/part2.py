from ordered_enum import OrderedEnum



filename = "input.txt"




# ---------------------------------------- HELPERS ----------------------------------------
class Type(OrderedEnum):
    FIVE_OF_A_KIND = 1
    # FIVE_OF_A_KIND_JOKER = 2
    FOUR_OF_A_KIND = 2
    # FOUR_OF_A_KIND_JOKER = 4
    FULL_HOUSE = 3
    # FULL_HOUSE_JOKER = 6
    THREE_OF_A_KIND = 4
    # THREE_OF_A_KIND_JOKER = 8
    TWO_PAIR = 5
    # TWO_PAIR_JOKER = 10
    ONE_PAIR = 6
    # ONE_PAIR_JOKER = 12
    HIGH_CARD = 7

    # HIGH_CARD_JOKER = 14

class Card:
    values = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

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
        self.type = self.get_type(self.cards)
        self.best_cards = self.get_best_cards()
        # self.get_type_cards()

    def get_type(self, cards):
        # Five of a kind
        if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]:
            # for cardee in cards:
            #     if cardee.value == "J": return Type.FIVE_OF_A_KIND_JOKER
            return Type.FIVE_OF_A_KIND
        # Four of a kind
        for i in range(0, 2):
            card1 = cards[i]
            count = 0
            for j in range(i+1, len(cards)):
                card2 = cards[j]
                if card1 == card2:
                    count += 1
                    if count == 3:
                        # for cardee in cards:
                        #     if cardee.value == "J": return Type.FOUR_OF_A_KIND_JOKER
                        return Type.FOUR_OF_A_KIND
        # Full house
        if (cards[0] == cards[1] == cards[2] and cards[3] == cards[4]) or (cards[0] == cards[1] and cards[2] == cards[3] == cards[4]):
            # for cardee in cards:
            #     if cardee.value == "J": return Type.FULL_HOUSE_JOKER
            return Type.FULL_HOUSE
        # Three of a kind
        for i in range(0, 3):
            card1 = cards[i]
            count = 0
            for j in range(i+1, len(cards)):
                card2 = cards[j]
                if card1 == card2:
                    count += 1
                    if count == 2:
                        # for cardee in cards:
                        #     if cardee.value == "J": return Type.THREE_OF_A_KIND_JOKER
                        return Type.THREE_OF_A_KIND
        # Two pair
        while (True):        
            break_index = 0
            pairs = 0
            for i in range(0, 4):
                card1 = cards[i]
                for j in range(i+1, len(cards)):
                    card2 = cards[j]
                    if card1 == card2:
                        break_index = j
                        pairs += 1
            for i in range(break_index, 4):
                card1 = cards[i]
                for j in range(i+1, len(cards)):
                    card2 = cards[j]
                    if card1 == card2:
                        pairs += 1
            if pairs == 2:
                # for cardee in cards:
                #     if cardee.value == "J": return Type.TWO_PAIR_JOKER
                return Type.TWO_PAIR
            break                
        # One pair
        for i in range(0, 4):
            if cards[i] == cards[i+1]:
                # for cardee in cards:
                #     if cardee.value == "J": return Type.ONE_PAIR_JOKER
                return Type.ONE_PAIR
        # High card
        # for cardee in cards:
        #     if cardee.value == "J": return Type.HIGH_CARD_JOKER
        return Type.HIGH_CARD

    def check_type(self, new_type):
        if new_type == Type.FIVE_OF_A_KIND: new_type = Type.FIVE_OF_A_KIND_JOKER
        if new_type == Type.FOUR_OF_A_KIND: new_type = Type.FOUR_OF_A_KIND_JOKER
        if new_type == Type.FULL_HOUSE: new_type = Type.FULL_HOUSE_JOKER
        if new_type == Type.THREE_OF_A_KIND: new_type = Type.THREE_OF_A_KIND_JOKER
        if new_type == Type.TWO_PAIR: new_type = Type.TWO_PAIR_JOKER
        if new_type == Type.ONE_PAIR: new_type = Type.ONE_PAIR_JOKER
        if new_type == Type.HIGH_CARD: new_type = Type.HIGH_CARD_JOKER
        return new_type

    def get_best_cards(self):
        values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        cards = self.true_cards.copy()
        joker_indices = []
        for i in range(0, len(cards)):
            if cards[i].value == "J":
                joker_indices.append(i)
        for i in range(0, len(joker_indices)):
            real_cardi = cards[joker_indices[i]]
            for valuei in values:
                cards[joker_indices[i]] = Card(valuei)
                sorted_cards = cards.copy()
                sorted_cards.sort()
                new_type = self.get_type(sorted_cards)
                if new_type < self.type:
                    self.type = new_type
                for j in range(i+1, len(joker_indices)):
                    real_cardj = cards[joker_indices[j]]
                    for valuej in values:
                        cards[joker_indices[j]] = Card(valuej)
                        sorted_cards = cards.copy()
                        sorted_cards.sort()
                        new_type = self.get_type(sorted_cards)
                        if new_type < self.type:
                            self.type = new_type
                        for k in range(j+1, len(joker_indices)):
                            real_cardk = cards[joker_indices[k]]
                            for valuek in values:
                                cards[joker_indices[k]] = Card(valuek)
                                sorted_cards = cards.copy()
                                sorted_cards.sort()
                                new_type = self.get_type(sorted_cards)
                                if new_type < self.type:
                                    self.type = new_type
                                for l in range (k+1, len(joker_indices)):
                                    real_cardl = cards[joker_indices[l]]
                                    for valuel in values:
                                        cards[joker_indices[l]] = Card(valuel)
                                        sorted_cards = cards.copy()
                                        sorted_cards.sort()
                                        new_type = self.get_type(sorted_cards)
                                        if new_type < self.type:
                                            self.type = new_type
                                    cards[joker_indices[l]] = real_cardl
                            cards[joker_indices[k]] = real_cardk
                    cards[joker_indices[j]] = real_cardj
            cards[joker_indices[i]] = real_cardi
        # for i in range(0, 5):
        #     card = cards[i]
        #     if card.value == "J":
        #         best_value = card
        #         for value in values:
        #             cards[i] = Card(value)
        #             new_type = self.get_type(cards)
        #             if new_type == Type.FIVE_OF_A_KIND: new_type = Type.FIVE_OF_A_KIND_JOKER
        #             if new_type == Type.FOUR_OF_A_KIND: new_type = Type.FOUR_OF_A_KIND_JOKER
        #             if new_type == Type.FULL_HOUSE: new_type = Type.FULL_HOUSE_JOKER
        #             if new_type == Type.THREE_OF_A_KIND: new_type = Type.THREE_OF_A_KIND_JOKER
        #             if new_type == Type.TWO_PAIR: new_type = Type.TWO_PAIR_JOKER
        #             if new_type == Type.ONE_PAIR: new_type = Type.ONE_PAIR_JOKER
        #             if new_type == Type.HIGH_CARD: new_type = Type.HIGH_CARD_JOKER
        #             if new_type < self.type:
        #                 self.type = new_type
        #                 best_value = value
        #         cards[i] = Card(best_value)

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
        for card in self.true_cards:
            if card.value == "J":
                return "{} {} ... JOKER".format(self.type, self.true_cards)
        return "{} {}".format(self.type, self.true_cards)

    def __repr__(self):
        for card in self.true_cards:
            if card.value == "J":
                return "{} {} ... JOKER".format(self.type, self.true_cards)
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
    print(hand)

    sum += scalar * hand.bet
    scalar += 1
print(sum)
