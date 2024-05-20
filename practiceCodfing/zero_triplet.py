from collections import Counter

def zero_triplet(l):
    a = 0
    b = 1  # Initialize b before the loop
    i = 3
    k = [[]]  # Initialize k with an empty list, not with a list containing an empty string
    while b != len(l) - 1:  # Adjusted loop condition
        while i < len(l):  # Removed unnecessary range
            s = l[a] + l[b] + l[i]  # Removed unnecessary variable s
            y = []  # Removed unnecessary list
            if s == 0:
                y.append(l[a])
                y.append(l[b])
                y.append(l[i])
                if Counter(y) not in [Counter(j) for j in k]:  # Adjusted uniqueness check
                    k.append(y)
            i += 1  # Increment i inside the inner loop
        a += 1  # Increment a and b outside the inner loop
        b += 1
               
    print(k)                   

l = [-1, 1, 0, 1, -1, -2, -1, 0]
zero_triplet(l)
