#!/usr/bin/python3
"""python3 -c 'print(__import__("2-matrix_divided.py").__doc__)'
"""


def matrix_type_check(matrix):
    """python3 -c 'print(__import__("2-matrix_divided.py").matrix_divided)'
    """
    if isinstance(matrix, list):
        if all(isinstance(sublist, list) for sublist in matrix):
            return True
        return False
    return False


def matrix_divided(matrix, div):
    """python3 -c 'print__import__("2-matrix_divided.py").matrix_divided'
    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix_type_check(matrix):
        raise TypeError(error1)
    check_list = [type(c) for x in matrix for c in x]
    if any(item not in [int, float] for item in check_list):
        raise TypeError(error1)
    length = len(matrix[0])
    if not all(len(x) == length for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(x/div, 2) for x in a] for a in matrix]
    return result_matrix
