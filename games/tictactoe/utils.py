from .constants import PLAYER_X, PLAYER_O, BOARD_SIZE

def create_board():
    return [[str(BOARD_SIZE * r + c + 1) for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * (BOARD_SIZE * 2 - 1))
    print()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

def is_full(board):
    return all(cell in [PLAYER_X, PLAYER_O] for row in board for cell in row)
