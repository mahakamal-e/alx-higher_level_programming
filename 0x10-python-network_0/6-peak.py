#!/usr/bin/python3
""" a function that finds a peak """


def find_peak(list_of_integers):
    """ Function uses to find a peak of unsorted list:
        Arg: list_of_integers
    """
    if not list_of_integers or list_of_integers == []:
        return None
    start_at = 0
    end_at = len(list_of_integers) - 1
    while start_at < end_at:
        mid = (start_at + end_at) // 2
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            end_at = mid
        else:
            start_at = mid + 1

    return list_of_integers[start_at]
