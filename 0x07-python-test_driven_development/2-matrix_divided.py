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

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]
