from .utils import create_board, print_board, check_winner, is_full
from .player import switch_player
from .constants import PLAYER_X, PLAYER_O

def play_game():
    board = create_board()
    current_player = PLAYER_X

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a spot (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input! Enter a number from 1 to 9.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] in [PLAYER_X, PLAYER_O]:
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    play_game()