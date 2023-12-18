#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_newlist = []
    for i in range(list_length):
        try:
            my_newlist.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            my_newlist.append(0)
        except TypeError:
            print("wrong type")
            my_newlist.append(0)
        except IndexError:
            print("out of range")
            my_newlist.append(0)
    return my_newlist
