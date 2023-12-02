#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for iterat in range(len(my_string)):
        if my_string[iterat] == 'c' or my_string[iterat] == 'C':
            continue
        new_string += my_string[iterat]
    return new_string
