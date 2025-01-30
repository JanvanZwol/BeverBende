import random

from cards import *

class Deck():
    def __init__(self):
        self.construct_cards()
        random.shuffle(self.draw_pile)
        self.deck_pointer = 1

        self.top_discard = self.draw_pile[0]


    def construct_cards(self):
        cards = list()

        #Add 4 point cards of value 0 till 8
        for ii in range(0, 8 +1):
            for jj in range(4):
                cards.append(Point_card(ii))
        #Add 9 point cards of value 9
        for ii in range(9):
            cards.append(Point_card(9))

         #Add this when ready
        '''
        #Add 9 trade power cards
        for ii in range(9):
            cards.append(Power_card("trade"))
        #Add 7 peek power cards
        for ii in range(7):
            cards.append(Power_card("peek"))
        #Add 5 draw twice power cards
        for ii in range(5):
            cards.append(Power_card("draw twice"))
        '''

        self.draw_pile = cards

    def deal_cards(self):
        cards = self.draw_pile[self.deck_pointer: self.deck_pointer + 4]
        self.deck_pointer += 4
        return cards
    
    def show_top_discard(self):
        return self.top_discard
    
    def draw_top_deck(self):
        card = self.draw_pile[self.deck_pointer]
        self.deck_pointer += 1
        return card
    
    def discard_card(self, card):
        self.top_discard = card