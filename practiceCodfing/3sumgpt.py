l = [1, -1, 0, 2, -1, 2, 4]
l.sort()  # Sort the list to optimize the process

for i in range(len(l) - 2):
    if i > 0 and l[i] == l[i - 1]:
        continue  # Skip duplicate elements to avoid duplicate combinations

    left, right = i + 1, len(l) - 1
    while left < right:
        total = l[i] + l[left] + l[right]
        if total == 0:
            print(f"[{l[i]}, {l[left]}, {l[right]}]",end=", ")
            left += 1
            right -= 1
            # Skip duplicate elements to avoid duplicate combinations
            while left < right and l[left] == l[left - 1]:
                left += 1
            while left < right and l[right] == l[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
