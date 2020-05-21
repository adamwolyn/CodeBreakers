from collections import deque
import random


SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

class Card:
    # Card constructor
    def __init__(self, suit, value):
        if (suit not in SUITS or value not in VALUES):
            raise ValueError
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "({}, {})".format(self.suit, self.value)

    # Returns the suit of the card.
    def suit(self):
        return self.suit

    # Returns the value of the card.
    def value(self):
        return self.value


class Deck:

    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    def __init__(self):
        self.num = 52
        self.deck = deque()
        for s in SUITS:
            for v in VALUES:
                self.deck.appendleft(Card(s, v))


    # Returns the number of Cards in the Deck
    def num_cards(self):
        return self.num


    # Shuffles the deck of cards.
    def shuffle(self):
        random.shuffle(self.deck)

    # Returns the top Card in the deck, then puts it back.
    def peek(self):
        return self.deck[0]

    # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        self.num -= 1
        return self.deck.popleft()

    # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
        if (self.num >= 52):
            raise RuntimeError
        else:
            self.num += 1
            self.deck.appendleft(card)

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        print(self.deck)


d = Deck()
print(d.num_cards())
d.print_deck()
d.shuffle()
d.print_deck()
for i in range(48):
    print(d.draw())
print(d.num_cards())
c = d.draw()
print(d.num_cards())
d.print_deck()
d.add_card(c)
print(d.num_cards())
d.print_deck()
