#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        # Check if the input is a string and is not None
        return 0
    roman_to_integer_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000}
    # Dictionary mapping roman numerals
    sum_roman_num = 0
    # Initialize sum of roman numerals
    for i in range(len(roman_string)):
        roman_num = roman_to_integer_map[roman_string[i]]
        # Get the integer value of the roman numeral
        if i > 0 and roman_string[i - 1] == 'I' \
                and roman_num > roman_to_integer_map['I']:
            sum_roman_num += roman_num - 2 * roman_to_integer_map['I']
        # If the previous roman numeral is 'I'
        # and the current roman numeral is greater than 'I'
        else:
            sum_roman_num += roman_num
        # Add the value of the roman numeral to the sum
    return sum_roman_num
