import numpy as np
import pytest


@pytest.fixture(scope="package")
def valid_sudoku():
    return np.array(
        [
            [9, 4, 2, 6, 7, 1, 3, 8, 5],
            [7, 3, 8, 9, 4, 5, 1, 6, 2],
            [5, 1, 6, 2, 8, 3, 7, 9, 4],
            [8, 5, 4, 7, 2, 9, 6, 3, 1],
            [6, 7, 3, 5, 1, 4, 9, 2, 8],
            [2, 9, 1, 8, 3, 6, 5, 4, 7],
            [4, 2, 9, 3, 5, 7, 8, 1, 6],
            [3, 8, 5, 1, 6, 2, 4, 7, 9],
            [1, 6, 7, 4, 9, 8, 2, 5, 3],
        ]
    )


@pytest.fixture(scope="package")
def masked_valid_sudoku(valid_sudoku):
    masked_sudoku = valid_sudoku.copy()
    for a in range(0, 8):
        masked_sudoku[a][a] = 0
    return masked_sudoku


@pytest.fixture(scope="package")
def unsolvable_sudoku():
    return np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 8, 7, 0, 1, 0, 0, 0, 0],
            [6, 5, 4, 0, 0, 0, 2, 0, 0],
            [8, 7, 9, 0, 0, 0, 0, 0, 0],
            [5, 4, 6, 0, 0, 0, 0, 0, 0],
            [2, 3, 1, 0, 0, 0, 0, 1, 0],
            [7, 9, 8, 0, 0, 0, 0, 0, 0],
            [4, 6, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
        ]
    )
