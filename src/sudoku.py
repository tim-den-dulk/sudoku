# Annotations are new functionality from python 3.10.,
# which allows us to use the class as a type inside the class.
from __future__ import annotations

from typing import Union

import attr
import numpy as np


@attr.s
class Sudoku:
    """
    A sudoku is a 9 by 9 array split into 3 by 3 boxes, which contains the numbers 1 to 9 once
    in each row, column, and 3 by 3 box.

    '0' is used as a placeholder for values not yet defined.
    """

    data = attr.ib(type=np.ndarray(shape=(9, 9), dtype=int))

    @data.validator
    def _validate_data_structure(self, attribute, data):
        if data.shape != (9, 9):
            raise ValueError("sudoku not a 9 by 9 array")
        if np.nanmin(data) < 0 or np.nanmax(data) > 9:
            raise ValueError(
                f"sudoku values should fall between 0-9. "
                f"min value: {np.nanmin(data)}. max value: {np.nanmax(data)}"
            )

    @classmethod
    def add_number(cls, old_sudoku: Sudoku, position: list, number: int) -> Sudoku:
        """
        Create a sudoku from an existing sudoku with the number in the specified position replaced.
        """
        new_sudoku = old_sudoku.data.copy()
        new_sudoku[position[0], position[1]] = number
        return cls(data=new_sudoku)

    def is_valid(self) -> bool:
        """ "
        tests whether any row, column, or 3 by 3 box contains any duplicate numbers.

        :returns: False if any duplicates are found. True if the sudoku is valid so far.
        """
        for row_or_column_number in range(0, 8):
            if (
                np.max(np.bincount(self.data[row_or_column_number, :])[1:], initial=0)
                > 1
                or np.max(
                    np.bincount(self.data[:, row_or_column_number])[1:], initial=0
                )
                > 1
            ):
                return False
        for box_number_row in range(0, 9, 3):
            for box_number_column in range(0, 9, 3):
                if (
                    np.max(
                        np.bincount(
                            self.data[
                                box_number_row : box_number_row + 3,
                                box_number_column : box_number_column + 3,
                            ].flatten()
                        )[1:],
                        initial=0,
                    )
                    > 1
                ):
                    return False
        return True

    def solve(self) -> Union[bool, Sudoku]:
        """
        Solvers are to be implemented in child classes.
        Currently available solvers: BruteForceSolver.
        Others may become available in the future.
        """
        raise NotImplementedError
