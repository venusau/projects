n = int(input("Enter the number of strings to be checked: "))
s = []
for i in range(n):
    s.append(input("Enter the string to be appended in the list: "))
k, c = "", 0
while c < len(min(s)):
    d = 1  # Assume the character is common initially
    for i in range(n - 1):
        if s[i][c] != s[i + 1][c]:
            d = 0  # If any character is not common, set d to 0 and break
            break
    if d == 1:
        k = k + s[0][c]  # Append the common character to k
        c += 1
    else:
        break  # If any character is not common, break the loop
print(f"Longest common prefix: {k}")
