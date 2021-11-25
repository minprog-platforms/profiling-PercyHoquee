import sys
import os
sys.path.append(os.path.abspath('.'))

import pytest  # noqa: E402 # ignore that this import is not top-level

from sudoku import Sudoku  # noqa: E402 # ignore that this import is not top-level


@pytest.fixture
def sudoku1():
    puzzle = [
        "7,9,0,0,0,0,3,0,1",
        "0,0,0,0,0,6,9,0,0",
        "8,0,0,0,3,0,0,7,6",
        "0,0,0,0,0,5,0,0,2",
        "0,0,5,4,1,8,7,0,0",
        "4,0,0,7,0,0,0,0,0",
        "6,1,0,0,9,0,0,0,8",
        "0,0,2,3,0,0,0,0,0",
        "0,0,9,0,0,0,0,5,4"
    ]
    puzzle = [row.replace(",", "") for row in puzzle]
    return Sudoku(puzzle)


@pytest.fixture
def sudoku2():
    puzzle = [
        "2,0,4,1,0,0,0,0,0",
        "0,0,0,5,0,3,6,0,7",
        "0,0,0,9,0,0,4,0,0",
        "9,0,0,4,3,0,0,1,0",
        "6,5,0,0,1,0,0,7,4",
        "0,2,0,0,0,8,0,0,9",
        "8,0,9,0,0,5,0,0,0",
        "5,0,2,3,0,1,0,0,0",
        "0,0,0,0,0,4,1,0,2",
    ]
    puzzle = [row.replace(",", "") for row in puzzle]
    return Sudoku(puzzle)


@pytest.fixture
def sudoku1_solved():
    puzzle = [
        "7,9,6,8,5,4,3,2,1",
        "2,4,3,1,7,6,9,8,5",
        "8,5,1,2,3,9,4,7,6",
        "1,3,7,9,6,5,8,4,2",
        "9,2,5,4,1,8,7,6,3",
        "4,6,8,7,2,3,5,1,9",
        "6,1,4,5,9,7,2,3,8",
        "5,8,2,3,4,1,6,9,7",
        "3,7,9,6,8,2,1,5,4"
    ]
    puzzle = [row.replace(",", "") for row in puzzle]
    return Sudoku(puzzle)


def test_value_at(sudoku1):
    assert sudoku1.value_at(0, 0) == 7
    assert sudoku1.value_at(0, 2) == 8
    assert sudoku1.value_at(8, 8) == 4
    assert sudoku1.value_at(5, 3) == 5


def test_row_values(sudoku1):
    assert list(sorted(sudoku1.row_values(0))) == [0, 0, 0, 0, 0, 1, 3, 7, 9]
    assert list(sorted(sudoku1.row_values(3))) == [0, 0, 0, 0, 0, 0, 0, 2, 5]
    assert list(sorted(sudoku1.row_values(8))) == [0, 0, 0, 0, 0, 0, 4, 5, 9]


def test_column_values(sudoku1):
    assert list(sorted(sudoku1.column_values(0))) == [0, 0, 0, 0, 0, 4, 6, 7, 8]
    assert list(sorted(sudoku1.column_values(3))) == [0, 0, 0, 0, 0, 0, 3, 4, 7]
    assert list(sorted(sudoku1.column_values(8))) == [0, 0, 0, 0, 1, 2, 4, 6, 8]


def test_block_values(sudoku1):
    assert list(sorted(sudoku1.block_values(0))) == [0, 0, 0, 0, 0, 0, 7, 8, 9]
    assert list(sorted(sudoku1.block_values(3))) == [0, 0, 0, 0, 0, 0, 0, 4, 5]
    assert list(sorted(sudoku1.block_values(8))) == [0, 0, 0, 0, 0, 0, 4, 5, 8]


def test_is_solved(sudoku1, sudoku2, sudoku1_solved):
    assert not sudoku1.is_solved()
    assert not sudoku2.is_solved()
    assert sudoku1_solved.is_solved()


def test_next_empty_index(sudoku1, sudoku2, sudoku1_solved):
    assert sudoku1.next_empty_index() == (2, 0)
    assert sudoku2.next_empty_index() == (1, 0)
    assert sudoku1_solved.next_empty_index() == (-1, -1)


def test_place(sudoku1):
    assert sudoku1.value_at(2, 0) == 0
    sudoku1.place(3, 2, 0)
    assert sudoku1.value_at(2, 0) == 3


def test_unplace(sudoku1):
    assert sudoku1.value_at(1, 0) == 9
    sudoku1.unplace(1, 0)
    assert sudoku1.value_at(1, 0) == 0


def test_options_at(sudoku1):
    assert list(sorted(sudoku1.options_at(2, 0))) == [4, 6]
    assert list(sorted(sudoku1.options_at(5, 3))) == [3, 9]
    assert list(sorted(sudoku1.options_at(6, 8))) == [1, 2, 6]
