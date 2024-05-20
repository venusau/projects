def generate_parentheses(n):
    result = []
    
    # Recursive helper function to generate parentheses
    def generate(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            generate(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            generate(current + ")", open_count, close_count + 1)
    
    generate("", 0, 0)
    return result

# Example usage:
n = 3
print(generate_parentheses(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
