from algebry.structures import Matrix, Vector
from algebry.systems import SLAR
matrix = Matrix(
    matrix=[[1, 2, -3, 4], [2, 2, -2, 3], [0, 1, 1, 0], [1, -1, 1, -2]]
)
xs = Vector([0, 0, 0, 0])

bs = Matrix(matrix=[[12], [10], [-1], [-4]])

slar = SLAR(matrix, xs, bs)
slar.solve_Gaus()

print('xs')
print(xs)



