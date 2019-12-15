from typing import List

Matrix = List[List[float]]


class Exes:
    def __init__(self, matrix: Matrix, filled_matrix: Matrix):
        self.matrix = matrix
        self.filled_matrix = filled_matrix

    def get_exes(self) -> float:
        value = 0
        for matrix_row, filled_row in zip(self.matrix, self.filled_matrix):
            for matrix_el, filled_el in zip(matrix_row, filled_row):
                if filled_el is not None:
                    value += matrix_el * filled_el
        return value
