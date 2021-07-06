import numpy as np

from src.brute_force_solver import BruteForceSolver
from tests.fixtures import masked_valid_sudoku, unsolvable_sudoku, valid_sudoku


def test_brute_force_solver(valid_sudoku, masked_valid_sudoku):
    expected = valid_sudoku
    actual = BruteForceSolver(masked_valid_sudoku).solve()

    np.testing.assert_array_almost_equal(actual.data, expected)


def test_unsolvable_sudoku(unsolvable_sudoku):
    expected = False
    actual = BruteForceSolver(unsolvable_sudoku).solve()

    assert actual == expected
