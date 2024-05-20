def myPow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = abs(n)
        return x * myPow(x, n - 1)
    else:
        return x * myPow(x, n - 1)

# Test cases
print(myPow(2.00000, 10))  # Output: 1024.00000
print(myPow(2.10000, 3))    # Output: 9.26100
print(myPow(2.00000, -2))   # Output: 0.25000
