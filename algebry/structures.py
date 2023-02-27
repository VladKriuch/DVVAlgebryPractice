from algebry.utils import *


class Matrix:
    def __init__(self, rows_counter=None, columns_counter=None, matrix=None):
        if matrix:
            if is_matrix(matrix):
                self.matrix = matrix
                self.rows_counter, self.columns_counter = get_rows_and_columns_counters(matrix)
                print('self.rows_counter')
                print(self.rows_counter)
            else:
                raise ValueError('Matrix must be a list of equal sized lists of integers or floats')

        elif rows_counter and columns_counter:
            if isinstance(rows_counter, int) and rows_counter >= 1 \
                    and isinstance(columns_counter, int) and columns_counter >= 1:
                self.matrix = generate_zeros_matrix(rows_counter, columns_counter)
                self.rows_counter, self.columns_counter = rows_counter, columns_counter
            else:
                raise ValueError('Rows counter and columns counter must be integer values greater than 0')

    def __add__(self, other):
        if self.rows_counter == other.rows_counter and self.columns_counter == other.columns_counter:
            result_matrix = []
            for row_index in range(self.rows_counter):
                row = []
                for column_index in range(self.columns_counter):
                    row.append(self.matrix[row_index][column_index] + other.matrix[row_index][column_index])
                result_matrix.append(row)

            return Matrix(result_matrix)
        else:
            raise ValueError('Matrices must be same size for the addition operation')

    def __sub__(self, other):
        if self.rows_counter == other.rows_counter and self.columns_counter == other.columns_counter:
            result_matrix = []
            for row_index in range(self.rows_counter):
                row = []
                for column_index in range(self.columns_counter):
                    row.append(self.matrix[row_index][column_index] - other.matrix[row_index][column_index])
                result_matrix.append(row)

            return Matrix(result_matrix)
        else:
            raise ValueError('Matrices must be same size for the addition operation')

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.columns_counter == other.rows_counter:
            result_matrix = generate_zeros_matrix(self.rows_counter, other.columns_counter)

            for row_index in range(self.rows_counter):
                for column_index in range(other.columns_counter):
                    for value_indx in range(self.columns_counter):
                        result_matrix[row_index][column_index] += \
                            self.matrix[row_index][value_indx] * other.matrix[value_indx][column_index]

            return Matrix(result_matrix)
        else:
            raise ValueError('Columns counter of the first matrix must be equal to rows counter of the second matrix')

    def __str__(self):
        representation_string = ''
        for row in self.matrix:
            for value in row:
                representation_string += str(value) + ' '

            representation_string += '\n'

        return representation_string

    def read_matrix_from_file(self, filepath=''):
        try:
            with open(filepath, 'r') as file:
                lines = file.read().splitlines()
                result_matrix = []
                for line in lines:
                    row = [float(num) for num in line.split()]
                    result_matrix.append(row)

                if is_matrix(result_matrix):
                    self.matrix = result_matrix
                    self.rows_counter, self.columns_counter = get_rows_and_columns_counters(result_matrix)
                else:
                    raise ValueError('Invalid matrix format')
        except Exception as err:
            raise ValueError('Invalid matrix format')

    def write_matrix_to_file(self, filepath=''):
        try:
            if not self.matrix:
                raise ValueError('No matrix to write')

            with open(filepath, 'a+') as file:
                file.write(str(self))
        except Exception as err:
            raise err

    def randomize_matrix(self, rows_counter, columns_counter, min_value=0, max_value=10000):
        if rows_counter >= 1 and columns_counter >= 1 and 0 <= min_value < max_value:
            self.matrix = generate_random_numbers_matrix(rows_counter, columns_counter, min_value, max_value)
            self.rows_counter, self.columns_counter = rows_counter, columns_counter
        else:
            raise ValueError('Incorrect values')

    def zeros_matrix(self, rows_counter, columns_counter):
        if rows_counter >= 1 and columns_counter >= 1:
            self.matrix = generate_zeros_matrix(rows_counter, columns_counter)
            self.rows_counter, self.columns_counter = rows_counter, columns_counter
        else:
            raise ValueError('Incorrect values')

    def calculate_matrix_norm(self):
        if not self.matrix_norm:
            self.matrix_norm = calculate_Euclid_matrix_norm(self.matrix)

        return self.matrix_norm


class Vector:
    def __init__(self, vector=None, vector_length=None):
        if vector:
            if isinstance(vector, list) and len(vector) >= 1 \
                    and all(isinstance(element, int) or isinstance(element, float) for element in vector):
                self.vector = vector
                self.length = len(vector)
            else:
                raise ValueError('Vector input should be a list of integers or floats')
        elif vector_length:
            if isinstance(vector_length, int) and vector_length >= 1:
                self.vector = [0 for _ in range(vector_length)]
            else:
                raise ValueError('Vector length must be an integer greater than zero')

    def __add__(self, other):
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            return calculate_vectors_sum(self.vector, other.vector)
        else:
            raise ValueError('Vectors must be an equal size for this operation')

    def __sub__(self, other):
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            return calculate_vectors_diff(self.vector, other.vector)
        else:
            raise ValueError('Vectors must be an equal size for this operation')

    def __mul__(self, other):
        raise ValueError('Not implemented error')

    def __str__(self):
        representation_string = ''
        for element in self.vector:
            representation_string += str(element) + ' '

        return representation_string

    def __len__(self):
        if self.vector:
            return len(self.vector)

    def read_from_file(self, filepath=''):
        try:
            with open(filepath, 'r') as file:
                vector_in_string = file.readline()
                vector = [float(num) for num in vector_in_string]
                self.vector = vector
                self.length = len(vector)
        except Exception as err:
            raise err

    def write_to_file(self, filepath=''):
        try:
            if not self.vector:
                raise ValueError('Nothing to write')

            with open(filepath, 'a+') as file:
                file.write(str(self))
        except Exception as err:
            raise err

    def ones_vector(self, length):
        if isinstance(length, int) and length >= 1:
            self.vector = [1 for _ in range(length)]
        else:
            raise ValueError('Length must be an integer more than zero')
