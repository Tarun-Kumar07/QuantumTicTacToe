from game.board import Board
from game.coordinate import Coordinate
from game.constants import O, LENGTH, X
import pytest


@pytest.mark.parametrize("column", [0, 1, 2])
def test_winner_column(column):
    board = Board()
    for i in range(LENGTH):
        coordinate = Coordinate(i, int(column))
        board.set(coordinate, O)

    assert board.get_winner() == O


@pytest.mark.parametrize("row", [0, 1, 2])
def test_winner_row(row):
    board = Board()
    for i in range(LENGTH):
        coordinate = Coordinate(int(row), i)
        board.set(coordinate, O)

    assert board.get_winner() == O


def test_winner_diagonal():
    board = Board()
    for i in range(LENGTH):
        coordinate = Coordinate(i, i)
        board.set(coordinate, X)

    assert board.get_winner() == X


def test_winner_off_diagonal():
    board = Board()
    for i in range(LENGTH):
        coordinate = Coordinate(i, LENGTH - i - 1)
        board.set(coordinate, X)

    assert board.get_winner() == X


def test_board_should_not_have_winner_when_created():
    board = Board()

    assert board.get_winner() is None


def test_board_should_have_no_winner_when_all_are_collapsed():
    board = Board()

    board.set(Coordinate(0, 0), X)
    board.set(Coordinate(0, 1), O)
    board.set(Coordinate(0, 2), O)
    board.set(Coordinate(1, 0), O)
    board.set(Coordinate(1, 1), O)
    board.set(Coordinate(1, 2), X)
    board.set(Coordinate(2, 0), X)
    board.set(Coordinate(2, 1), X)
    board.set(Coordinate(2, 2), O)
    # X 0 0
    # 0 0 X
    # X X 0

    assert board.all_tiles_collapsed() is True
    assert board.get_winner() is None


def test_board_should_have_no_winner():
    board = Board()

    board.set(Coordinate(0, 0), X)
    board.set(Coordinate(0, 1), X)
    # X X Q
    # Q Q Q
    # Q Q Q

    assert board.get_winner() is None
