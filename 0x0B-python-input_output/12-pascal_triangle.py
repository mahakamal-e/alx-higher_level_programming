#!/usr/bin/python3
""" define pascal_triangle """


def pascal_triangle(n):
    """ Impelmentation """
    if n <= 0:
        return []
    arr_ = [[1]]
    while len(arr_) != n:
        last_element = arr_ [-1]
        tmp = [1]
        for i in range(len(last_element) - 1):
            tmp.append(last_element[i] + last_element[i + 1])
        tmp.append(1)
        arr_.append(tmp)
    return arr_
