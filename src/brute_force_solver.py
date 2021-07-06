from __future__ import annotations
import attr
import numpy as np
from typing import Union
from src.sudoku import Sudoku


@attr.s
class BruteForceSolver(Sudoku):
    def solve(self) -> Union[bool, Sudoku]:
        for x in range(1, 10):
            next_step = BruteForceSolver.add_number(self, self._next_empty_cell(), x)
            if next_step.is_valid():
                if not next_step._next_empty_cell():
                    return next_step
                followup = next_step.solve()
                if isinstance(followup, Sudoku):
                    return followup
            if x == 9:
                return False

    def _next_empty_cell(self):
        empty_cells = np.where(self.data == 0)
        if empty_cells[0].size == 0:
            return False
        return [empty_cells[0][0], empty_cells[1][0]]
