#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # abs - get last digit as +ve, ignore -ve sign

if number < 0:
    last_digit = -last_digit  # Re-assign -ve
print("Last digit of {} is".format(number), end=" ")  # Print the last digit

# Assign each to a specific case
if last_digit == 0:
    print("0 and is 0")
elif last_digit > 5:
    print("{} and is greater than 5".format(last_digit))
else:
    print("{} and is less than 6 but not 0".format(last_digit))
