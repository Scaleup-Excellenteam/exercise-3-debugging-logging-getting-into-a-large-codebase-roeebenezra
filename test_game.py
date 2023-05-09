from chess_engine import game_state
from enums import Player
from Piece import Knight


def test_knight_valid_peaceful_moves():
    # Set up the game state
    gs = game_state()

    # Set up the knight
    white_knight = Knight('n', 3, 4, Player.PLAYER_2)

    # Set up Empty board
    gs.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]

    # Set Knight on the board
    gs.board[3][4] = white_knight

    # Get the moves for the knight
    moves = white_knight.get_valid_peaceful_moves(gs)

    # # Assert that the expected moves are in the list
    expected_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]

    assert set(moves) == set(expected_moves)


def test_knight_valid_peaceful_moves_blocked():
    # Set up the game state
    gs = game_state()

    # Set up the knight
    white_knight = Knight('n', 3, 4, Player.PLAYER_2)

    # Set Knight on the board
    gs.board[3][4] = white_knight

    # Get the moves for the knight
    moves = white_knight.get_valid_peaceful_moves(gs)

    # # Assert that the expected moves are in the list
    expected_moves = [(2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]

    assert set(moves) == set(expected_moves)


def test_knight_valid_piece_takes():
    # Set up the game state
    gs = game_state()

    # Set up the knight
    white_knight = Knight('n', 3, 4, Player.PLAYER_2)

    # Get the takes moves for the knight
    moves = white_knight.get_valid_piece_takes(gs)

    # # Assert that the expected moves are in the list
    expected_moves = [(1, 3), (1, 5)]

    assert set(moves) == set(expected_moves)


def test_valid_piece_moves():
    # Set up the game state
    gs = game_state()

    # Set up the knight
    white_knight = Knight('n', 3, 4, Player.PLAYER_2)

    # Set Knight on the board
    gs.board[3][4] = white_knight

    # Get the moves for the knight
    moves = white_knight.get_valid_piece_moves(gs)

    # # Assert that the expected moves are in the list
    expected_moves = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)]

    assert set(moves) == set(expected_moves)
