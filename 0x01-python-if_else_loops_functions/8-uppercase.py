#!/usr/bin/python3
def uppercase(str):
    for c_ in str:
        value_ = ord(c_)
        if 97 <= value_ <= 122:
            value_ = value_ - 32
            print("{}".format(chr(value_)), end="")
    print("")
