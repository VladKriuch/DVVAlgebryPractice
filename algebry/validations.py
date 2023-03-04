def validate_slar_sizes(matrix, vector_xs, vector_bs):
    return matrix.columns_counter == len(vector_xs) and matrix.rows_counter == vector_bs.rows_counter and \
        all(len(row) == 1 for row in vector_bs.matrix)
