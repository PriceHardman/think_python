# Exercise 18-6.
# The following are the possible hands in poker, in increasing
# order of value (and decreasing order of probability):

# pair:    two cards with the same rank

# two pair:    two pairs of cards with the same rank

# three of a kind:    three cards with the same rank

# straight: five cards with ranks in sequence (aces can be high or low, so
# Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-
# King-Ace-2-3 is not.)

# flush:    five cards with the same suit

# full house:    three cards with one rank, two cards with another

# four of a kind:    four cards with the same rank

# straight flush: five cards in sequence (as defined above) and with the same
# suit

# The goal of these exercises is to estimate the probability of drawing these
# various hands.

# Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True
# or False according to whether or not the hand meets the relevant criteria.
# Your code should work correctly for “hands” that contain any number of cards
# (although 5 and 7 are the most common sizes).

# Write a method named classify that figures out the highest-value
# classification for a hand and sets the label attribute accordingly. For
# example, a 7-card hand might contain a flush and a pair; it should be labeled
# “flush.”


# When you are convinced that your classification methods are working, the next
# step is to estimate the probabilities of the various hands. Write a function
# in PokerHand.py that shuffles a deck of cards, divides it into hands,
# classifies the hands, and counts the number of times various classifications
# appear.

# => See probability_simulation() at bottom

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

    suit_names = [
        "Clubs","Diamonds","Hearts","Spades"
    ]
    rank_names = [
        None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"
    ]

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

    def sort(self):
        self.cards.sort()

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,n_hands,n_cards,poker_hands=False):
        """Deals PokerHands if poker_hands is True"""
        hands = []
        for i in range(n_hands):
            if poker_hands:
                hand = PokerHand()
            else:
                hand = Hand()
            self.move_cards(hand,n_cards)
            hands.append(hand)
        return hands

class Hand(Deck):
    """Class for a hand of cards. Inherits from Deck."""
    def __init__(self,label=''):
        self.cards = []
        self.label = label

    def __contains__(self,other_card):
        """Returns True if other_card is in the hand"""
        for card in self.cards:
            if card == other_card:
                return True
        return False

class PokerHand(Hand):

    def suit_count(self):
        suits = {0:0,1:0,2:0,3:0}
        for card in self.cards:
            suits[card.suit] += 1
        return suits

    def rank_count(self):
        ranks = {i:0 for i in range(1,14)}
        for card in self.cards:
            ranks[card.rank] += 1
        return ranks

    def has_pair(self):
        if len([v for (k,v) in self.rank_count().items() if v==2]) == 1:
            return True
        else:
            return False

    def has_two_pair(self):
        if len([v for (k,v) in self.rank_count().items() if v==2]) >= 2:
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        if len([v for (k,v) in self.rank_count().items() if v==3]) >= 1:
            return True
        else:
            return False

    def has_straight(self,return_straight=False):
        """
            Returns boolean indicating whether the player has a straight.
            If return_straight is flagged True, also returns a list
            of the straights.
        """
        ranks = [k for (k,v) in self.rank_count().items() if v > 0]
        possible_straights = [
            list(range(i,i+5)) for i in ranks if i+5-1 <= ranks[-1]
        ]
        straights = []
        for possible_straight in possible_straights:
            if set(possible_straight).issubset(set(ranks)):
                straights.append([
                    card for card in self.cards
                    if card.rank in possible_straight
                ])

        if len(straights) > 0:
            if return_straight:
                return (True, straights)
            else:
                return True
        else:
            if return_straight:
                return (False,straights)
            else:
                return False

    def has_flush(self,return_flush=False):
        """
            Returns boolean indicating whether the player has a flush.
            If return_flush is flagged True, also returns a list of all cards
            of the flush suit.
        """
        flush_suit = [k for (k,v) in self.suit_count().items() if v>=5]
        if len(flush_suit) >= 1:
            if return_flush:
                return (
                    True,
                    [card for card in self.cards if card.suit == flush_suit[0]]
                )
            else:
                return True
        else:
            if return_flush:
                return (False,[])
            else:
                return False

    def has_full_house(self):
        if self.has_pair() and self.has_three_of_a_kind():
            return True
        else:
            return False

    def has_four_of_a_kind(self):
        if len([v for (k,v) in self.rank_count().items() if v==4]) >= 1:
            return True
        else:
            return False

    def has_straight_flush(self):
        has_straight, straights = self.has_straight(True)
        has_flush, flush = self.has_flush(True)
        if has_straight and has_flush:
            flush_cards = Hand()
            flush_cards.cards = flush
            for straight in straights:
                for card in straight:
                    if card not in flush_cards:
                        return False
            return True
        else:
            return False

    def classify(self):
        """
            Sets the self.label attribute according to the highjest-valued
            hand the player can make.
        """
        label = ''
        if self.has_straight_flush():
            label = 'straight flush'
        elif self.has_four_of_a_kind():
            label = 'four of a kind'
        elif self.has_full_house():
            label = 'full house'
        elif self.has_flush():
            label = 'flush'
        elif self.has_straight():
            label = 'straight'
        elif self.has_three_of_a_kind():
            label = 'three of a kind'
        elif self.has_two_pair():
            label = 'two pair'
        elif self.has_pair():
            label = 'pair'
        else:
            label = 'no hand'
        self.label = label
        return


def simulate_probabilities(n_iter=1000,n_cards=7):
    """
        Records the frequencies of each hand as a best hand by
        dealing one hand with n_cards cards, recording the best hand
        that can be made, and repeating n_iter times.
    """
    hands = [
        'no hand',
        'pair',
        'two pair',
        'three of a kind',
        'straight',
        'flush',
        'full house',
        'four of a kind',
        'straight flush'
    ]

    freqs = {hand:0 for hand in hands}

    for i in range(n_iter):
        deck = Deck()
        deck.shuffle()
        hand = deck.deal_hands(1,n_cards,True)[0] # deal one PokerHand
        hand.classify()
        freqs[hand.label] += 1

    probs = {key: (freq/n_iter) for (key,freq) in freqs.items()}
    for hand in hands:
        print("P(%s) = %0.4f" % (hand, probs[hand]))
    return


simulate_probabilities(10000)

# =>

# P(no hand) = 0.1832
# P(pair) = 0.4360
# P(two pair) = 0.2322
# P(three of a kind) = 0.0493
# P(straight) = 0.0420
# P(flush) = 0.0315
# P(full house) = 0.0238
# P(four of a kind) = 0.0020
# P(straight flush) = 0.0000
