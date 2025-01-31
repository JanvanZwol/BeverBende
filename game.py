from deck import *
from cards import *
from player import *
from strategies import *
from gameState import *

class Game():
    def __init__(self, strategies):
        self.deck = Deck()
        self.num_players = len(strategies)
        
        self.players = list()
        for ii in range(self.num_players):
            self.players.append(Player(self.deck, strategies[ii]))

    def check_game_end(self, next_player):
        deck_depleted = self.deck.deck_pointer == len(self.deck.draw_pile)
        player_stopped = next_player.stop
        return deck_depleted or player_stopped
    
    def play(self, verbose = False, turn_indicator = True):
        game_state = Game_state(self)

        while not self.check_game_end(self.players[game_state.player_turn]):
            current_player = self.players[game_state.player_turn]
            private_game_state = Private_game_state(game_state, game_state.player_turn)

            if verbose or turn_indicator:
                print(f"Player {game_state.player_turn}'s turn")

            #Check first descision
            first_decision = current_player.strategy.first_decision(private_game_state)
                
            if verbose:
                print(f"picks {first_decision}")
            
            #resolve second descision
            if first_decision == "A":
                card_in_hand = self.deck.show_top_discard()
                second_decision = current_player.strategy.second_decision_A(private_game_state, card_in_hand)
                current_player.replace_card(second_decision, card_in_hand)
                game_state.player_card_discovered(game_state.player_turn, second_decision, card_in_hand)

            elif first_decision == "B":
                card_in_hand = self.deck.draw_top_deck()
                second_decision = current_player.strategy.second_decision_B(private_game_state, card_in_hand)
                if second_decision == 4:
                    self.deck.discard_card(card_in_hand)
                else:
                    current_player.replace_card(second_decision, card_in_hand)
                    game_state.player_card_unkown(game_state.player_turn, second_decision)

            if verbose:
                print(f"picks {second_decision}")

            #Check whether to stop
            stop_decision = current_player.strategy.stop_decision(private_game_state)
            current_player.stop = stop_decision
            if stop_decision:
                game_state.last_turn_called()

            if verbose and stop_decision:
                    print("elected to stop")

            game_state.next_turn()
    
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

Game([Human_interface(), Naive_strategy()]).play()