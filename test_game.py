import unittest

from chess_engine import game_state
from enums import Player
from Piece import Knight
from Piece import Bishop
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

    def test_bishop_valid_peaceful_moves_blocked(self):
        # Set up the Bishop
        white_bishop = Bishop('b', 3, 4, Player.PLAYER_2)

        # Set Bishop on the board
        self.gs.board[3][4] = white_bishop

        # Get the moves for the Bishop
        moves = white_bishop.get_valid_peaceful_moves(self.gs)

        # Assert that the expected moves are in the list
        expected_moves = [(4, 3), (2, 3), (4, 5), (2, 5)]

    def test_bishop_valid_peaceful_moves(self):
        # Set up the Bishop
        white_bishop = Bishop('b', 3, 4, Player.PLAYER_2)

        # Get the moves for the Bishop
        moves = white_bishop.get_valid_peaceful_moves(self.gs)

        # Assert that the expected moves are in the list
        expected_moves = [(4, 3), (2, 3), (4, 5), (5, 6), (2, 5), (5, 2)]

        assert set(moves) == set(expected_moves)

    def test_knight_valid_piece_takes_blocked(self):
        # Set up the knight
        white_knight = Knight('n', 3, 4, Player.PLAYER_2)

        # Set Knight on the board
        self.gs.board[3][4] = white_knight

        # Get the moves for the knight
        moves = white_knight.get_valid_piece_takes(self.gs)

        # # Assert that the expected moves are in the list
        expected_moves = [(1, 3), (1, 5)]

        assert set(moves) == set(expected_moves)

    def test_knight_valid_piece_takes(self):
        # Set up the knight
        white_knight = Knight('n', 3, 4, Player.PLAYER_2)

        # Get the takes moves for the knight
        moves = white_knight.get_valid_piece_takes(self.gs)

        # # Assert that the expected moves are in the list
        expected_moves = [(1, 3), (1, 5)]

        assert set(moves) == set(expected_moves)

    def test_bishop_valid_piece_takes_blocked(self):
        # Set up the Bishop
        white_bishop = Bishop('b', 3, 4, Player.PLAYER_2)

        # Set Bishop on the board
        self.gs.board[3][4] = white_bishop

        # Get the moves for the Bishop
        moves = white_bishop.get_valid_piece_takes(self.gs)

        # Assert that the expected moves are in the list
        expected_moves = [(1, 6), (1, 2)]

        assert set(moves) == set(expected_moves)

    # Integration tests
    def test_valid_piece_moves(self):
        # Set up the bishop
        white_bishop = Knight('b', 3, 4, Player.PLAYER_2)

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

    # System tests
    def test_stupid_mate(self):
        self.gs.move_piece((1, 2), (2, 2), False)  # Move white pawn
        self.gs.move_piece((6, 3), (5, 3), False)  # Move black pawn
        self.gs.move_piece((1, 1), (3, 1), False)  # Move white pawn
        self.gs.move_piece((7, 4), (3, 0), False)  # Move black queen
        # Check if the black player created checkmate
        assert self.gs.checkmate_stalemate_checker() == 0
