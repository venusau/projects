# Define the function roman_to_int
def roman_to_int(s):
    # Create a dictionary to map Roman numerals to integers
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Initialize the result variable to store the final integer value
    result = 0
    # Initialize the prev_value variable to keep track of the previous value during iteration
    prev_value = 0

    # Iterate over the characters of the input string in reverse order
    for char in s[::-1]:
        # Get the integer value of the current Roman numeral character from the dictionary
        curr_value = roman_map[char]
        # Check if the current value is less than the previous value
        if curr_value < prev_value:
            # If so, subtract the current value from the result
            result -= curr_value
        else:
            # Otherwise, add the current value to the result
            result += curr_value
        # Update the prev_value variable for the next iteration
        prev_value = curr_value

    # Return the final result
    return result

# Test the function with example inputs
print(roman_to_int("LLLLC"))        # Output: 3
print(roman_to_int("LVIII"))      # Output: 58
print(roman_to_int("MCMXCIV"))    # Output: 1994
