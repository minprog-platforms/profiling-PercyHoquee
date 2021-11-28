from __future__ import annotations
from typing import Iterable, List
from functools import lru_cache


class Sudoku:
    """A mutable sudoku puzzle."""

    def __init__(self, puzzle: Iterable[Iterable]):
        self._grid: list[str] = []

        for puzzle_row in puzzle:
            row = ""

            for element in puzzle_row:
                row += str(element)

            self._grid.append(row)

        self._rows: List[List[int]] = []

        self._columns: List[List[int]] = []

        # initialize empty lists because multiple blocks at a time are being filled  # noqa: E501
        self._blocks: List[List[int]] = [[], [], [], [], [], [], [], [], []]

        # add values in original sudoku to their position in rows, columns, and blocks  # noqa: E501
        for i in range(9):
            new_row = []
            new_column = []

            for j in range(9):
                row_number = int(self._grid[i][j])

                column_number = int(self._grid[j][i])

                # calculates to which block certain coordinates belong
                number_of_block = block_number(j, i)

                new_row.append(row_number)

                new_column.append(column_number)

                self._blocks[number_of_block].append(row_number)

            self._rows.append(new_row)

            self._columns.append(new_column)

    def place(self, value: int, x: int, y: int) -> None:
        """Place value at x,y."""

        self._rows[y][x] = value
        self._columns[x][y] = value

        number_of_block = block_number(x, y)
        # calculates the index of certain coordinates in their block
        index_in_block = block_index(x, y)

        self._blocks[number_of_block][index_in_block] = value

    def unplace(self, x: int, y: int) -> None:
        """Remove (unplace) a number at x,y."""

        self._rows[y][x] = 0
        self._columns[x][y] = 0

        number_of_block = block_number(x, y)
        index_in_block = block_index(x, y)

        self._blocks[number_of_block][index_in_block] = 0

    def value_at(self, x: int, y: int) -> int:
        """Returns the value at x,y."""
        value = self._rows[y][x]

        return value

    def options_at(self, x: int, y: int) -> Iterable[int]:
        """Returns all possible values (options) at x,y."""

        options = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        # Remove all values from the row
        for value in self._rows[y]:
            if value in options:
                options.remove(value)

        # Remove all values from the column
        for value in self._columns[x]:
            if value in options:
                options.remove(value)

        # Get the index of the block based from x,y
        number_of_block = block_number(x, y)

        # Remove all values from the block
        for value in self._blocks[number_of_block]:
            if value in options:
                options.remove(value)

        return options

    def next_empty_index(self) -> tuple[int, int]:
        """
        Returns the next index (x,y) that is empty (value 0).
        If there is no empty spot, returns (-1,-1)
        """
        next_x, next_y = -1, -1

        for i in range(9):
            for j in range(9):
                if self._rows[i][j] == 0:
                    return j, i

        return next_x, next_y

    def row_values(self, i: int) -> Iterable[int]:
        """Returns all values at i-th row."""
        values = self._rows[i]

        return values

    def column_values(self, i: int) -> Iterable[int]:
        """Returns all values at i-th column."""

        values = self._columns[i]

        return values

    def block_values(self, i: int) -> Iterable[int]:
        """
        Returns all values at i-th block.
        The blocks are arranged as follows:
        0 1 2
        3 4 5
        6 7 8
        """
        values = self._blocks[i]

        return values

    def is_solved(self) -> bool:
        """
        Returns True if and only if all rows, columns and blocks contain
        only the numbers 1 through 9. False otherwise.
        """

        values = list(range(1, 10))

        result = True

        # removing first loop leads to first or last rows breaking rules
        for i in range(9):
            for value in values:
                if value not in self.row_values(i):
                    result = False

                if value not in self.column_values(i):
                    result = False

                if value not in self.block_values(i):
                    result = False

        i = 0

        # updating self._grid to solved sudoku
        for row in self._rows:
            self._grid[i] = "".join(str(digit) for digit in row)

            i += 1

        return result

    def __str__(self) -> str:
        representation = ""

        for row in self._grid:
            representation += row + "\n"

        return representation.strip()


@lru_cache(maxsize=1)
def load_from_file(filename: str) -> Sudoku:
    """Load a Sudoku from filename."""
    puzzle: list[str] = []

    with open(filename) as f:
        for line in f:

            # strip newline and remove all commas
            line = line.strip().replace(",", "")

            puzzle.append(line)

    return Sudoku(puzzle)


def block_number(x: int, y: int) -> int:
    """ returns to which block certain coordinates belong """
    number = (x // 3) + ((y // 3) * 3)

    return number


def block_index(x: int, y: int) -> int:
    """ returns the index wihtin a block of certain coordinates """
    number = (x % 3) + ((y % 3) * 3)

    return number
