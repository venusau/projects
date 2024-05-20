str = "xxxxxxxxxmalayalamx"

if len(str) == 0:
    print("Invalid input!!")
elif len(str) == 1:
    print(f"Longest palindromic substring: {str}")
else:
    max_length = 1
    start = 0

    for i in range(len(str)):
        # Check for odd-length palindromes
        l = i
        r = i
        while l >= 0 and r < len(str) and str[l] == str[r]:
            if (r - l + 1) > max_length:
                start = l
                max_length = r - l + 1
            l -= 1
            r += 1

        # Check for even-length palindromes
        l = i
        r = i + 1
        while l >= 0 and r < len(str) and str[l] == str[r]:
            if (r - l + 1) > max_length:
                start = l
                max_length = r - l + 1
            l -= 1
            r += 1

    print(f"Longest palindromic substring: {str[start:start + max_length]}")
