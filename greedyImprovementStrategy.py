from abc import ABC, abstractmethod

from strategies import Strategy

class Greedy_improvement_strategy(Strategy):
    @staticmethod
    def first_decision(game_state):
        top_discard = game_state.show_top_discard().points
        highest_points, highest_index = Greedy_improvement_strategy.highest_visible_card(game_state)
        
        if top_discard < highest_points:
            return 0
        else:
            return 1

    
    @staticmethod
    def second_decision_A(game_state, card_in_hand):
        highest_points, highest_index = Greedy_improvement_strategy.highest_visible_card(game_state)
        return highest_index
    
    @staticmethod
    def second_decision_B(game_state, card_in_hand):
        highest_points, highest_index = Greedy_improvement_strategy.highest_visible_card(game_state)
        has_invisible, invisible_index = Greedy_improvement_strategy.first_invisible_card(game_state)
        if (card_in_hand.points >= highest_points and not has_invisible) or card_in_hand.points == 9:
            return 4
        elif card_in_hand.points < highest_points:
            return highest_index
        else:
            return invisible_index
    
    @staticmethod
    def stop_decision(game_state):
        return False

    @staticmethod
    def highest_visible_card(game_state):
        highest_points = -1
        highest_index = -1

        for ii in range(4):
            card = game_state.my_cards[ii]
            if card != None:
                if card.points > highest_points:
                    highest_points = card.points
                    highest_index = ii

        return highest_points, highest_index
    
    @staticmethod
    def first_invisible_card(game_state):

        for ii in range(4):
            card = game_state.my_cards[ii]
            if card == None:
                return True, ii
            
        return False, -1