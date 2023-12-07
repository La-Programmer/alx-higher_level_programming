#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        holder = list(map(lambda x: pow(x, 2), matrix[i]))
        square_matrix.append(holder)
    return square_matrix
