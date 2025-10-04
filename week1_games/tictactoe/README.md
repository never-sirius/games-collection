## **Tic Tac Toe**
A simple Tic Tac Toe game built in Python.
This is part of the Game Collection Project, where each week a new game is developed to practice programming fundamentals.

## **Features**
2-player mode (play with a friend in the terminal).
Clean board display in the console.
Input validation (prevents invalid or repeated moves).
Detects wins (rows, columns, diagonals) and draws.

## **Code Overview**

Board Display

The game board is a 3×3 grid stored in a list of lists.
print_board() prints the current state after each move.

Game Logic

check_winner() checks rows, columns, and diagonals for a win.
is_full() checks if the board is completely filled (draw).

Main loop alternates turns between X and O.

## **Concepts Practiced**

Lists (2D arrays) to store board state
Loops & conditionals for turn logic
Functions to organize game checks
Input handling & validation