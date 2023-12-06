#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_ = []
        for i in row:
            row_.append(i ** 2)
        new_matrix.append(row_)
    return(new_matrix)
