from __future__ import annotations

from typing import Union

import attr
import numpy as np

from src.sudoku import Sudoku


@attr.s
class BruteForceSolver(Sudoku):
    """
    A Brute Force Sudoku Solver.
    Uses trial and error together with backtracking to find a solution for the sudoku.
    """

    def solve(self) -> Union[bool, Sudoku]:
        """
        Selects the first empty square and tries incremental numbers until a number fits.
        Once it finds a valid number, it moves on to the next square and tries to find a fit.
        When the solver finds no valid solution for a square, it backtracks
        and increases the previous empty square by 1.

        :returns: either a solved Sudoku instance, or False when no solution is possible.
        """

        for number in range(1, 10):
            next_step = BruteForceSolver.add_number(
                self, self._next_empty_cell(), number
            )
            if next_step.is_valid():
                if not next_step._next_empty_cell():
                    return next_step
                followup = next_step.solve()
                if isinstance(followup, Sudoku):
                    return followup
            if number == 9:
                return False

    def _next_empty_cell(self):
        """ "
        finds and returns the first cell that is empty (has a zero value)
        """
        empty_cells = np.where(self.data == 0)
        if empty_cells[0].size == 0:
            return False
        return [empty_cells[0][0], empty_cells[1][0]]
