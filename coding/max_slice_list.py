def slice_with_greatest_sum(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0
    max_substring = []  # Initialize max_substring to an empty list
    current_substring = []  # Initialize current_substring to an empty list

    # Iterate through the list of numbers
    for num in nums:
        # Update current_sum to include the current number
        current_sum += num
        current_substring.append(num)  # Add the current number to current_substring
        
        # Update max_sum and max_substring if current_sum becomes greater than max_sum
        if current_sum > max_sum:
            max_sum = current_sum
            max_substring = current_substring.copy()  # Update max_substring
        
        # Reset current_sum and current_substring to empty lists if current_sum becomes negative
        if current_sum < 0:
            current_sum = 0
            current_substring = []

    return max_sum, max_substring

# Test the function
nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum, max_substring = slice_with_greatest_sum(nums)
print("Maximum sum:", max_sum)
print("Substring with maximum sum:", max_substring)
