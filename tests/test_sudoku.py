import numpy as np
import pytest

from src.sudoku import Sudoku
from tests.fixtures import masked_valid_sudoku, valid_sudoku


def test_sudoku_valid_format(valid_sudoku):
    assert Sudoku(valid_sudoku).is_valid()


def test_sudoku_invalid_format():
    with pytest.raises(ValueError) as e_info:
        Sudoku(np.array([1, 2, 3]))


def test_sudoku_outlier_numbers(valid_sudoku):
    invalid_sudoku = valid_sudoku
    invalid_sudoku[0][0] = 12
    with pytest.raises(ValueError) as e_info:
        Sudoku(invalid_sudoku)


def test_partial_sudoku(masked_valid_sudoku):
    assert Sudoku(masked_valid_sudoku).is_valid()
