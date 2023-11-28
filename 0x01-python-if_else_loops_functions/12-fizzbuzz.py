#!/usr/bin/python3
def fizzbuzz():
    for iterat in range (1, 101):
        if iterat % 3:
            print("Fizz", end="")
        elif iterat % 5:
            print("Buzz", end=" ")
        elif iterat % 3 and iterat % 5:
            print("FizzBuzz", end=" ")
        else:
            print(iterat, end=" ")
