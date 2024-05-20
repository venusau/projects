def letter_combinations(digits):
    if not digits:
        return []

    # Create a mapping of digits to letters
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Recursive function to generate combinations
    def generate_combinations(index, path):
        if index == len(digits):
            combinations.append(path)
            return

        for letter in letters[digits[index]]:
            generate_combinations(index + 1, path + letter)

    combinations = []
    generate_combinations(0, '')
    return combinations

# Test cases
print(letter_combinations("23456789"))  
print(letter_combinations("2"))   
