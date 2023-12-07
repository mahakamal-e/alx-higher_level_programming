#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum_1 = 0
        sum_2 = 0
        for a, b in my_list:
            sum_1 += a * b
        for a, b in my_list:
            sum_2 += b
        return sum_1 / sum_2
