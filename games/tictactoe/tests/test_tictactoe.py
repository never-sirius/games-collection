import unittest
from games.tictactoe.utils import create_board
from games.tictactoe.tictactoe import check_winner, is_full
from games.tictactoe.player import switch_player

class TestTicTacToe(unittest.TestCase):
    def test_switch_player(self):
        self.assertEqual(switch_player("X"), "O")
        self.assertEqual(switch_player("O"), "X")

    def test_board_creation(self):
        board = create_board()
        self.assertEqual(len(board), 3)
        self.assertEqual(len(board[0]), 3)

if __name__ == "__main__":
    unittest.main()