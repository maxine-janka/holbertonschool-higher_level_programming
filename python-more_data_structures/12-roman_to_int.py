#!/usr/bin/python3
def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer """

    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num_result = 0
    for i in range(len(roman_string)):
        # Check next char is not the last one
        # and check if current is less than next
        if (i + 1 < len(roman_string)
        and roman[roman_string[i]] < roman[roman_string[i + 1]]):
            # if yes, subtract it from the current value
            num_result -= roman[roman_string[i]]
        else:
            # Otherwise add the value
            num_result += roman[roman_string[i]]

    return num_result
