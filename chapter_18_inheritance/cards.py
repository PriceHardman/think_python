# Implementation of Playing Cards

import random

class Card(object):
    """Represents a standard playing card."""
    def __init__(self,suit=0,rank=2):
        """
            suit: {0,1,2,3} -> {C,H,D,S},
            rank: {0,2..10,11,12,13} -> {A,2..10,J,Q,K}
            default = 2C (2 of clubs)
        """
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs","Diamonds","Hearts","Spades"]
    rank_names = [None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank],Card.suit_names[self.suit])

    def __lt__(self,other):
        if self.rank != other.rank: return (self.rank < other.rank)
        return (self.suit < other.suit)

    def __eq__(self,other):
        return ((self.rank == other.rank) and (self.suit == other.suit))


class Deck(object):
    """A collection of Card objects"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self):
        card_list = []
        for card in self.cards:
            card_list.append(str(card))
        return '\n'.join(card_list)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,n_hands,n_cards):
        hands = []
        for i in range(n_hands):
            hand = Hand()
            self.move_cards(hand,n_cards)
            hands.append(hand)
        return hands



class Hand(Deck):
    """Class for a hand of cards. Inherits from Deck."""
    def __init__(self,label=''):
        self.cards = []
        self.label = label

deck = Deck()
deck.shuffle()
hands = deck.deal_hands(3,7)
for i,hand in enumerate(hands):
    print("\nHand %d:" % (i+1))
    print(hand)
