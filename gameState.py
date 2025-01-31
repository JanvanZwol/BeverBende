class Game_state():
    def __init__(self, game):
        self.game = game
        self.players = game.players
        self.num_players = len(game.players)
        self.deck = game.deck
        self.player_turn = 0
        self.round = 0
        self.last_turn = False

        self.public_cards = dict()
        for ii in range(self.num_players):
            self.public_cards[ii] = [None, None, None, None]

    def next_turn(self):
        self.player_turn = (self.player_turn + 1) % self.num_players
        if self.player_turn == 0:
            self.round += 1

    def player_card_discovered(self, player_index, card_index, card):
        self.public_cards[player_index][card_index] = card

    def player_card_unkown(self, player_index, card_index):
        self.public_cards[player_index][card_index] = None

    def last_turn_called(self):
        self.last_turn = True

class Private_game_state():
    def __init__(self, game_state, player_index):
        self.my_index = player_index
        self.public_cards = game_state.public_cards
        self.num_players = game_state.num_players
        self.round = game_state.round
        self.cards_left = len(game_state.deck.draw_pile) - game_state.deck.deck_pointer
        self.top_discard = game_state.deck.show_top_discard()

        self.my_cards = [None, None, None, None]
        this_player = game_state.players[player_index]
        for ii in range(4):
            if this_player.visible[ii]:
                self.my_cards[ii] = this_player.cards[ii]

    def my_cards_to_string(self):
        res = ""
        for card in self.my_cards:
            if card != None:
                res += str(card.points)
            else:
                res += "?"
        return res
    
    def show_top_discard(self):
        return self.top_discard