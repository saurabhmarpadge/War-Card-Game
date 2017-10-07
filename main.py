from random import shuffle

SUITE = 'Heart Diamond Shape Club'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

class Hand:
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}\n".format(self.name,drawn_card))
        return drawn_card


    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hands.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


print('Welcome to War Game')
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

comp = Player("computer",Hand(half1))

name = input("What is your name?")
user = Player(name,Hand(half2))

total_round = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_round += 1
    print("Time for a new round!")
    print("here are the current stands")
    print(user.name + "has the count: "+str(len(user.hand.cards)))
    print(comp.name + "has the count: "+str(len(comp.hand.cards)))
    print("Play the card!\n")

    table_cards = []

    c_card = comp.play_card()
    u_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(u_card)

    if c_card[1] == u_card[1]:
        war_count += 1

        print("There is a war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

if(comp.still_has_cards()):
    print("Computer Wins!!!")
else:
    print(user.name+" Wins!!!")
