#!/usr/bin/python3
def uppercase(str):
    for c_ in str:
        if ord(c_) > 96 and ord(c_) < 123:
            print("{:c}".format(ord(c_) - 32), end="")
    print("")
