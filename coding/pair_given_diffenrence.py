l = []

n = int(input("Enter the length of the list: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))

x = int(input("Enter the absolute difference: "))

found_pair = False

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if abs(l[i] - l[j]) == x:
            print(1)
            found_pair = True
            break
    if found_pair:
        break

if not found_pair:
    print(-1)
