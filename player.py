from cards import *
from deck import *

class Player():
    def __init__(self, deck):
        self.deck = deck
        self.cards = deck.deal_cards()
        self.visible = [True, False, False, True]
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

class Human_Player(Player):
    def __init__(self, deck):
        super().__init__(deck)

    def first_decision_strategy(self):
        help_statement = "show cards\nshow discard\ndraw discard\ndraw deck"

        while True:
            print("It's your turn")
            inp = input("> ").lower()

            if inp == "show cards":
                print(f"Your cards are: {self.cards_to_string()}")
            elif inp == "show discard":
                print(f"Top card on the discard pile is: {self.deck.show_top_discard()}")
            elif inp == "draw discard":
                return "A"
            elif inp == "draw deck":
                return "B"
            else:
                print(help_statement)

    def second_decision_A_strategy(self, card_in_hand):
        help_statement = "show cards\nshow discard\n0,1,2,3 to pick a card to replace"

        while True:
            print(f"You have an {str(card_in_hand)} in hand")
            inp = input("> ").lower()

            #Improvised case switch
            if inp == "show cards":
                print(f"Your cards are: {self.cards_to_string()}")
            elif inp == "show discard":
                print(f"Top card on the discard pile is: {self.deck.show_top_discard()}")
            elif inp in "0123" and len(inp) == 1:
                return int(inp)
            else:
                print(help_statement)

    def second_decision_B_strategy(self, card_in_hand):
        help_statement = "show cards\nshow discard\n0,1,2,3 to pick a card to replace\n4 to discard"

        while True:
            print(f"You have an {str(card_in_hand)} in hand")
            inp = input("> ").lower()

            #Improvised case switch
            if inp == "show cards":
                print(f"Your cards are: {self.cards_to_string()}")
            elif inp == "show discard":
                print(f"Top card on the discard pile is: {self.deck.show_top_discard()}")
            elif inp in "01234" and len(inp) == 1:
                return int(inp)
            else:
                print(help_statement)

    def stop_decision_strategy(self):
        help_statement = "show cards\nshow discard\nstop or yes or y\nno or n)"

        while True:
            print(f"Do you want to stop?")
            inp = input("> ").lower()

            #Improvised case switch
            if inp == "show cards":
                print(f"Your cards are: {self.cards_to_string()}")
            elif inp == "show discard":
                print(f"Top card on the discard pile is: {self.deck.show_top_discard()}")
            elif inp in ["stop", "yes", "y"]:
                return True
            elif inp in ["no", "n"]:
                return False
            else:
                print(help_statement)