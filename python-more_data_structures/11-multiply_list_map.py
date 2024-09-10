#!/usr/bin/python3
def multiply_list_map(my_list, number):
    return list(map(lambda x: x * number, my_list))
# the function lambda x: x * number multiplies each element
# of my_list by number
