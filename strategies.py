from abc import ABC, abstractmethod
import random

class Strategy():
    @staticmethod
    @abstractmethod
    def first_decision(self, game_state):
        pass
    
    @staticmethod
    @abstractmethod
    def second_decision_A(self, game_state, card_in_hand):
        pass
    
    @staticmethod
    @abstractmethod
    def second_decision_B(self, game_state, card_in_hand):
        pass
    
    @staticmethod
    @abstractmethod
    def stop_decision(self, game_state):
        pass

class Human_interface(Strategy):
    @staticmethod
    def first_decision(game_state):
        help_statement = "draw discard(A) or draw deck(B)"
        print(f"It's your turn\nYour cards are: {game_state.my_cards_to_string()}\nTop card on the discard pile is: {game_state.show_top_discard()}")

        while True:
            inp = input("> ").lower()
            if inp == "draw discard" or inp == "a":
                return "A"
            elif inp == "draw deck" or inp == "b":
                return "B"
            else:
                print(help_statement)

    @staticmethod
    def second_decision_A(game_state, card_in_hand):
        help_statement = "0,1,2,3 to pick a card to replace"

        while True:
            print(f"You have an {str(card_in_hand)} in hand")
            inp = input("> ").lower()

            #Improvised case switch
            if inp in "0123" and len(inp) == 1:
                return int(inp)
            else:
                print(help_statement)

    @staticmethod
    def second_decision_B(game_state, card_in_hand):
        help_statement = "0,1,2,3 to pick a card to replace or 4 to discard"

        while True:
            print(f"You have an {str(card_in_hand)} in hand")
            inp = input("> ").lower()

            #Improvised case switch
            if inp in "01234" and len(inp) == 1:
                return int(inp)
            else:
                print(help_statement)

    @staticmethod
    def stop_decision(game_state):
        help_statement = "To Stop: stop or yes or y\nOtherwise: no or n)"

        while True:
            print(f"Do you want to stop?")
            inp = input("> ").lower()

            #Improvised case switch
            if inp in ["stop", "yes", "y"]:
                return True
            elif inp in ["no", "n"]:
                return False
            else:
                print(help_statement)

class Naive_strategy(Strategy):
    @staticmethod
    def first_decision(pgame_state):
        return ["A", "B"][random.randint(0,1)]
    
    @staticmethod
    def second_decision_A(game_state, card_in_hand):
        return random.randint(0,3)
    
    @staticmethod
    def second_decision_B(game_state, card_in_hand):
        return random.randint(0,4)
    
    @staticmethod
    def stop_decision(game_state):
        return False