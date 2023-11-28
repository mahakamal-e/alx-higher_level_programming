#!/usr/bin/python3
for char_ in range(ord('z'), ord('a') - 1, -1):
    print('{:c}{:c}'.format((char_), (char_ - 33)), end='')
