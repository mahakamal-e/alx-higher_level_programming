#!/usr/bin/python3
for iterat in range(97, 123):
    if iterat == 113 or iterat == 101:
        continue
    print("{}".format(chr(iterat)), end="")
