#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(a_dictionary, key=a_dictionary.get)
        return max_score

    # max() returns the default value if there are no iterable objects
    # Doesn't return multiple keys if max score is the same
