from deck import *
from cards import *
from player import *

class Game():
    def __init__(self, num_players):
        self.deck = Deck()
        self.num_players = num_players
        
        self.players = list()
        for ii in range(num_players):
            self.players.append(Human_Player(self.deck))

    def check_game_end(self, next_player):
        deck_depleted = self.deck.deck_pointer == len(self.deck.draw_pile)
        player_stopped = next_player.stop
        return deck_depleted or player_stopped
    
    def play(self, verbose = False, turn_indicator = True):
        player_turn = 0

        while not self.check_game_end(self.players[player_turn]):
            current_player = self.players[player_turn]
            if verbose or turn_indicator:
                print(f"Player {player_turn}'s turn")

            #Check first descision
            first_decision = current_player.first_decision_strategy()
                
            if verbose:
                print(f"picks {first_decision}")
            
            #resolve second descision
            if first_decision == "A":
                card_in_hand = self.deck.show_top_discard()
                second_decision = current_player.second_decision_A_strategy(card_in_hand)
                current_player.replace_card(second_decision, card_in_hand)

            elif first_decision == "B":
                card_in_hand = self.deck.draw_top_deck()
                second_decision = current_player.second_decision_B_strategy(card_in_hand)
                if second_decision == 4:
                    self.deck.discard_card(card_in_hand)
                else:
                    current_player.replace_card(second_decision, card_in_hand)

            if verbose:
                print(f"picks {second_decision}")

            #Check whether to stop
            stop_decision = current_player.stop_decision_strategy()
            current_player.stop = stop_decision

            if verbose and stop_decision:
                    print("elected to stop")

            player_turn = (player_turn + 1) % self.num_players
    
        if verbose or turn_indicator:
            print("game ended")
            lowest_score = 37
            lowest_player = -1
            for ii in range(self.num_players):
                self.players[ii].calculate_score()
                if self.players[ii].score < lowest_score:
                    lowest_score = self.players[ii].score
                    lowest_player = ii
                print(f"Players {ii} has {self.players[ii].score} points")
            print(f"Player {lowest_player} won")

Game(2).play()