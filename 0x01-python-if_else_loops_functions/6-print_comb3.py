#!/usr/bin/python3
for start_ in range(10):
    for end_i in range(start_, 100):
            if start_ == 8 and end_i == 9:
                print("{:d}{:d}".format(start_, end_i))
            else:
                print("{:d}{:d}".format(start_, end_i), end=(", "))
