l=[]
n=int(input("Enter the length of the list : "))
k=0
for i in range(n):
    l.append(int(input(f"Enter the element to be appended at the index ({i}): ")))
    k=l[i]

for i in range(n):
    if k>l[i]:
        k=l[i]

print(f"The minimum element is : {k}")