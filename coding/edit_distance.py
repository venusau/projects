def min_operations(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],        # Remove operation
                                   dp[i][j - 1],        # Insert operation
                                   dp[i - 1][j - 1])   # Replace operation

    return dp[m][n]

s = input("Enter the first string: ")
t = input("Enter the second string: ")
print("Minimum number of operations required:", min_operations(s, t))
