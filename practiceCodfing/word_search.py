l = [["A", "B", "C", "E"],
     ["S", "F", "C", "S"],
     ["A", "D", "E", "E"]]

word = input("Enter the word to be searched : ")

a, b = 0, 0
k = word[0]
a = None
b = None

# Find the starting position of the word
for i in range(len(l)):
    if k in l[i]:
        a = i
        b = l[i].index(k)
        break

x = None
i = 1

# Search for the word in the grid
while i < len(word) and a < len(l) and b < len(l[0]):
    k = word[i]
    if b + 1 < len(l[0]) and k == l[a][b + 1]:
        b += 1
        i += 1
        x = True
    elif a + 1 < len(l) and k == l[a + 1][b]:
        a += 1
        i += 1
        x = True
    else:
        x = False
        break

if x==True:
    print("Word is present in the grid.")
else:
    print("Word is not present in the grid.")
