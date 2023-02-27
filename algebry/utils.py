import random
import math


def is_matrix(matrix_list):
    if isinstance(matrix_list, list) and len(matrix_list) >= 1:
        element_length = len(matrix_list[0])
        return all(is_matrix_row(element) and len(element) == element_length for element in matrix_list)
    return False


def is_matrix_row(row):
    return isinstance(row, list) and len(row) >= 1 and \
           all(isinstance(element, int) or isinstance(element, float) for element in row)


def get_rows_and_columns_counters(matrix):
    rows_counter = len(matrix)
    column_counter = len(matrix[0])

    return rows_counter, column_counter


def generate_zeros_matrix(rows_counter, columns_counter):
    return [[0 for j in range(columns_counter)] for i in range(rows_counter)]


def generate_random_numbers_matrix(rows_counter, columns_counter, min_value=0, max_value=10000):
    return [[random.randint(min_value, max_value) for j in range(columns_counter)] for i in range(rows_counter)]


def calculate_Euclid_matrix_norm(matrix):
    summ = 0
    for row in matrix:
        summ += sum(elem ** 2 for elem in row)

    return math.sqrt(summ)


def calculate_vectors_sum(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(len(vector1))]


def calculate_vectors_diff(vector1, vector2):
    return [vector1[i] - vector2[i] for i in range(len(vector1))]


def solve_linear_system(A, xs, b):
    n = len(A)

    # Combine A and b into an augmented matrix
    M = [[A[i][j] for j in range(n)] + [b[i][0]] for i in range(n)]

    # Apply Gaussian elimination with partial pivoting
    for i in range(n):
        # Find the pivot row with the largest absolute value in the i-th column
        pivot_row = max(range(i, n), key=lambda j: abs(M[j][i]))
        if pivot_row != i:
            M[i], M[pivot_row] = M[pivot_row], M[i]

        # Eliminate the i-th variable in lower rows
        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n + 1):
                M[j][k] -= factor * M[i][k]

    # Back-substitute to solve for xs
    for i in range(n - 1, -1, -1):
        xs[i] = (M[i][n] - sum(M[i][j] * xs[j] for j in range(i + 1, n))) / M[i][i]

    return xs

