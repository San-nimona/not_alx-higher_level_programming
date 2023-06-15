#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        A function that returns the squares of elements in a matrix


        Returns a new matrix

    '''
    new_lst = []
    if len(matrix) == 0:
        return new_lst

    new_lst = [[i*i for i in j] for j in matrix]
    return new_lst
