import unittest

from chess_engine import game_state
from enums import Player
from Piece import Knight
from ai_engine import chess_ai


class TestChessEngine(unittest.TestCase):
    def setUp(self):
        self.gs = game_state()

    # Unit tests
    def test_knight_valid_peaceful_moves(self):
        # Set up the knight
        white_knight = Knight('n', 3, 4, Player.PLAYER_2)

        # Set up Empty board
        self.gs.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]

        # Set Knight on the board
        self.gs.board[3][4] = white_knight

        # Get the moves for the knight
        moves = white_knight.get_valid_peaceful_moves(self.gs)

        # # Assert that the expected moves are in the list
        expected_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]

        assert set(moves) == set(expected_moves)

    def test_knight_valid_peaceful_moves_blocked(self):
        # Set up the knight
        white_knight = Knight('n', 3, 4, Player.PLAYER_2)

        # Set Knight on the board
        self.gs.board[3][4] = white_knight

        # Get the moves for the knight
        moves = white_knight.get_valid_peaceful_moves(self.gs)

        # # Assert that the expected moves are in the list
        expected_moves = [(2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]

        assert set(moves) == set(expected_moves)

    def test_knight_valid_piece_takes(self):
        # Set up the knight
        white_knight = Knight('n', 3, 4, Player.PLAYER_2)

        # Get the takes moves for the knight
        moves = white_knight.get_valid_piece_takes(self.gs)

        # # Assert that the expected moves are in the list
        expected_moves = [(1, 3), (1, 5)]

        assert set(moves) == set(expected_moves)

    # Integration tests
    def test_valid_piece_moves(self):
        # Set up the knight
        white_knight = Knight('n', 3, 4, Player.PLAYER_2)

        # Set Knight on the board
        self.gs.board[3][4] = white_knight

        # Get the moves for the knight
        moves = white_knight.get_valid_piece_moves(self.gs)

        # # Assert that the expected moves are in the list
        expected_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]

        assert set(moves) == set(expected_moves)

    # evaluate_board test for black player
    def test_evaluate_board_black_player(self):
        self.gs.board[6][0] = Player.EMPTY  # Remove opponent pawn, +10 points
        evaluate_board = chess_ai().evaluate_board(self.gs, Player.PLAYER_2)
        assert evaluate_board == 10


    # evaluate_board test for white player
    def test_evaluate_board_white_player(self):
        self.gs.board[1][0] = Player.EMPTY  # Remove opponent pawn, +10 points
        evaluate_board = chess_ai().evaluate_board(self.gs, Player.PLAYER_1)
        assert evaluate_board == 10
