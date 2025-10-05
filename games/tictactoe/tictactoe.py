def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def tic_tac_toe():
    board = [[str(3 * r + c + 1) for c in range(3)] for r in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a spot (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input! Enter a number from 1 to 9.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] in ["X", "O"]:
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

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
