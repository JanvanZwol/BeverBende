from cards import *
from deck import *

class Player():
    def __init__(self, deck, strategy):
        self.deck = deck
        self.cards = deck.deal_cards()
        self.visible = [True, False, False, True]

        self.strategy = strategy

        self.stop = False

    def cards_to_string(self):
        res = ""

        for ii in range(4):
            if self.visible[ii]:
                res += str(self.cards[ii])
            else:
                res += "?"

        return res
    
    def replace_card(self, card_index, card_in_hand):
        self.deck.discard_card(self.cards[card_index])
        self.cards[card_index] = card_in_hand
        self.visible[card_index] = True

    def calculate_score(self):
        self.score = 0
        for card in self.cards:
            self.score += card.points