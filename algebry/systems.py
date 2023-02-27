from algebry.structures import Matrix, Vector
from algebry.validations import validate_slar_sizes
from algebry.utils import *


class SLAR:
    def __init__(self, matrix: Matrix, vector_xs: Vector, matrix_bs: Matrix):
        if isinstance(matrix, Matrix) and isinstance(vector_xs, Vector) and isinstance(matrix_bs, Matrix):
            if validate_slar_sizes(matrix, vector_xs, matrix_bs):
                self.matrix = matrix
                self.vector_xs = vector_xs
                self.matrix_bs = matrix_bs
            else:
                raise ValueError('Incorrect sizes')
        else:
            raise ValueError('Incorrect inputs')

    def solve_Gaus(self):
        # form coef matrix
        solve_linear_system(self.matrix.matrix, self.vector_xs.vector, self.matrix_bs.matrix)
        return self.vector_xs.vector