from copy import deepcopy
from typing import List, Tuple

Matrix = List[List[float]]
Cell = Tuple[int, int]


class Cycle:

    plus = '+'
    minus = '-'
    was = [plus, minus, None]

    def __init__(self, matrix: 'Matrix', cell: Cell):
        self.matrix = matrix
        self.cycle = [[el for el in row] for row in matrix]
        self.cell = cell
        self.cycle_map = None

        self.n = len(matrix)
        self.m = len(matrix[0])

    def make_cycle(self) -> 'Matrix':
        self.create_cycle()
        self.create_map()

        delta = self.get_delta()
        x, y = self.cell
        self.matrix[x][y] = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.cycle_map[i][j] == self.plus:
                    self.matrix[i][j] += delta
                if self.cycle_map[i][j] == self.minus:
                    self.matrix[i][j] -= delta
                    if int(self.matrix[i][j]) == 0:
                        self.matrix[i][j] = None

        return self.matrix

    def create_cycle(self):
        x, y = self.cell
        self.cycle[x][y] = self.plus

        change = True

        while change:
            change = False
            for row in self.cycle:
                if sum(map(lambda el: el is not None, row)) == 1:
                    row[:] = [None] * len(row)
                    change = True
            for j in range(self.m):
                col = (row[j] for row in self.cycle)
                if sum(map(lambda el: el is not None, col)) == 1:
                    for row in self.cycle:
                        row[j] = None
                        change = True

    def create_map(self):
        self.cycle_map = deepcopy(self.cycle)
        x, y = self.cell
        self._paint_row(x, -1)

    def get_delta(self) -> float:
        min_el = min(el_cycle for row_cycle, row_map in zip(self.cycle, self.cycle_map)
                     for el_cycle, el_map in zip(row_cycle, row_map)
                     if el_cycle not in self.was and el_map == self.minus)
        return min_el

    def _paint_row(self, index: int, value: int):
        for i, el in enumerate(self.cycle_map[index]):
            if el not in self.was:
                self.cycle_map[index][i] = self.plus if value == 1 else self.minus
                self._paint_col(i, -value)

    def _paint_col(self, index: int, value: int):
        for i, row in enumerate(self.cycle_map):
            if row[index] not in self.was:
                row[index] = self.plus if value == 1 else self.minus
                self._paint_row(i, -value)