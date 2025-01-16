#!/usr/bin/python3
def fizzbuzz():
    """
    Prints the numbers from 1 to 100. For multiples of 3 print Fizz,
    for multiples of 5, print Buzz, for multiples of 3 and 5, print FizzBuzz.
    """
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
