#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
# Return the key with the biggest value in the dictionary with .get method
    return None
