def is_palindrome(s):
    # Returns True if the input string is a palindrome, False otherwise.
    return s == s[::-1]

l = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
palindrome_pairs = []

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        k = l[i] + l[j]
        if is_palindrome(k):
            palindrome_pairs.append((l[i], l[j]))

if not palindrome_pairs:
    print("No such pair.")
else:
    print(palindrome_pairs)