#!/usr/bin/python3
""" matrix module """


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix.

    Args:
       matrix: input matrix.
       div: number to divided matrix elements by.

    Return:
         new list that represents divided matrix
    Raises:
         TypeError: if matric not the list.
         or If div is not int or float.
         or sublists not all have same size.
         ZeroDivisionError: If div is zero.
    """

    if not all(isinstance(row, list) for row in matrix) or not\
            all(all(isinstance(num, (int, float))for num in row)\
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
