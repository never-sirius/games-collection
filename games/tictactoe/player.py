from .constants import PLAYER_X, PLAYER_O

def switch_player(current_player):
    return PLAYER_O if current_player == PLAYER_X else PLAYER_X
