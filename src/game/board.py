from copy import deepcopy

from game.coordinate import Coordinate
from game.constants import Q


class Board(object):
    def __init__(self) -> None:
        self.board = [[Q for _ in range(3)] for _ in range(3)]

    def get_winner(self):
        # Row
        for row in self.board:
            row_winner = self.__check_for_winner(row)
            if row_winner is not None:
                return row_winner

        # Column
        for col_index in range(3):
            column = self.get_column(col_index)
            column_winner = self.__check_for_winner(column)
            if column_winner is not None:
                return column_winner

        # Diagonals
        diag = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diag_winner = self.__check_for_winner(diag)
        if diag_winner is not None:
            return diag_winner

        off_diag = [self.board[0][2], self.board[1][1], self.board[2][0]]
        off_diag_winner = self.__check_for_winner(off_diag)
        if off_diag_winner is not None:
            return off_diag_winner

    def __check_for_winner(self, list):
        no_dups = set(list)
        if Q in list or len(no_dups) != 1:
            return None

        return no_dups.pop()

    def get_column(self, col_index):
        column = []
        for row in self.board:
            column.append(row[col_index])
        return column

    def all_tiles_collapsed(self):
        for row in self.board:
            for tile in row:
                if tile == Q:
                    return False
        return True

    def set(self, coordinate: Coordinate, value: str):
        self.board[coordinate.get_x()][coordinate.get_y()] = value

    def get(self, coordinate: Coordinate):
        return self.board[coordinate.get_x()][coordinate.get_y()]

    def get_all(self):
        return deepcopy(self.board)

    def __str__(self) -> str:
        return "\n".join([" ".join([str(tile) for tile in row]) for row in self.board])
