"""
Luke Mains
2018.July.21

Class for a deck of cards.
"""


class Deck:
    """
    Simulates a deck of cards.
    """

    def __init__(self):
        self.suits = 'cdhs'
        self.values = 'a23456789jqk'
        self.cards = self.build_deck()

    def build_deck(self):
        cards = []
        for suit in self.suits:
            for value in self.values:
                cards.append(value + ' of ' + suit)

        return cards
