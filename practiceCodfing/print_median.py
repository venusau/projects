def append_list(lst):
    lst.append(int(input("Enter the number to be appended in list : ")))

l1 = []
l2 = []

while True:
    choice = int(input("Enter 1 to append list 1 and 2 to append list 2 or 0 to break appending : "))
    if choice == 1:
        append_list(l1)
    elif choice == 2:
        append_list(l2)
    else:
        break

l1.sort()
l2.sort()

total_sum = sum(l1) + sum(l2)
total_count = len(l1) + len(l2)

median = total_sum / total_count

print("Sorted list 1:", l1)
print("Sorted list 2:", l2)
print(f"Median: {median}")
