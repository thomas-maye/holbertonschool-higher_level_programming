#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        # Check if the input is a string and is not None
        return 0
    roman_to_integer_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000}
    # Dictionary mapping roman numerals
    sum_roman_num = 0
    prev_roman_num = 0
    # Initialize sum of roman numerals and previous value
    for i in roman_string:
        current_roman_num = roman_to_integer_map.get(i, 0)
        # Get the value of the current roman numeral
        if current_roman_num > prev_roman_num:
            sum_roman_num += current_roman_num - 2 * prev_roman_num
            # If the current value is greater than the previous value,
            # subtract the previous value from the current value and add
            # it to the sum
        else:
            sum_roman_num += current_roman_num
            # Add the current value to the sum
        prev_roman_num = current_roman_num
        # Get the previous value

    return sum_roman_num
