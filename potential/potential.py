from typing import List, Optional, Tuple

Matrix = List[list]
Cell = Tuple[int, int]


class Potential:

    def __init__(self, matrix: Matrix, filled_matrix: Matrix):
        self.matrix = matrix
        self.filled_matrix = filled_matrix

        self.n = len(matrix)
        self.m = len(matrix[0])
        self.count_potential = self.n + self.m

        self.potential_matrix = [[0 for _ in range(self.count_potential + 1)] for _ in range(self.count_potential)]

    def get_potentials(self) -> Tuple[List[float], List[float]]:
        self.fill_potential_matrix()
        self.calculate_potential()

        potentials = [0 for _ in range(self.count_potential)]
        for row in self.potential_matrix:
            if (index := self.get_index(row[:-1])) is not None:
                potentials[index] = row[-1]

        u = potentials[:self.n]
        v = potentials[self.n:]

        return u, v

    def fill_potential_matrix(self):
        self.potential_matrix[0][0] = 1
        pos = 1
        for i, (matrix_row, filled_row) in enumerate(zip(self.matrix, self.filled_matrix)):
            for j, (matrix_el, filled_el) in enumerate(zip(matrix_row, filled_row)):
                if filled_el is not None:
                    self.potential_matrix[pos][i] = 1
                    self.potential_matrix[pos][self.n + j] = 1
                    self.potential_matrix[pos][-1] = matrix_el
                    pos += 1
                    if pos > self.count_potential:
                        raise ValueError(f'Filled cell > than n + m - 1: {self.n + self.m - 1}')

    def calculate_potential(self):
        for i, row in enumerate(self.potential_matrix):
            if self.check_alone_element(row[:-1]):
                self.reduce_rows(i)

    def reduce_rows(self, start: int):
        for i, row in enumerate(self.potential_matrix):
            index = self.get_index(self.potential_matrix[start])
            if row[index] == 1 and i != start:
                self.potential_matrix[i][index] = 0
                self.potential_matrix[i][-1] -= self.potential_matrix[start][-1]
                index = self.get_index(row[:-1])
                self.reduce_rows(i)

    @staticmethod
    def get_index(row: List[int]) -> int:
        for i, el in enumerate(row):
            if el != 0:
                return i

    @staticmethod
    def check_alone_element(row: List[float]) -> bool:
        return True if sum(row) == 1 else False

    def get_coords(self) -> Optional[Cell]:
        u, v = self.get_potentials()
        c_min_value = 0
        cell = None
        for i, (matrix_row, filled_row) in enumerate(zip(self.matrix, self.filled_matrix)):
            for j, (matrix_el, filled_el) in enumerate(zip(matrix_row, filled_row)):
                if filled_el is None:
                    c_value = matrix_el - (u[i] + v[j])
                    if c_value < c_min_value:
                        c_min_value = c_value
                        cell = (i, j)

        return cell
