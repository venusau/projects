def substring_satisfactory(substring, pattern):
    for char in pattern:
        if char not in substring:
            return False
    return True

S = input("Enter the String to checked : ")
P = input("Enter the String to be checked for : ")

pattern = list(P)
copy_s = S
shortest_substring = S

for i in range(len(S) - len(P) + 1):
    for j in range(len(P), len(S)):
        substring = copy_s[i:j + 1]
        if substring_satisfactory(substring, pattern) and len(substring) < len(shortest_substring):
            shortest_substring = substring

print("The shortest substring that contains the pattern is:", shortest_substring)