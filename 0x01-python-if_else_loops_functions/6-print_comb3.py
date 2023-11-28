#!/usr/bin/python3
for start_ in range(10):
    for end_i in range(start_ + 1, 10):
        if start_ == 8 and end_i == 9:
            print("{:02d}{:02d}".format(start_, end_i))
        else:
            print("{:02d}{:02d}".format(start_, end_i), end=", ")
