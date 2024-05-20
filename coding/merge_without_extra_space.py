l1=[]
l2=[]
n=int(input("Enter the length of the list 1"))
m=int(input("Enter the length of the list 2"))

for i in range(n):
    l1.append(int(input(f"Enter the element to append in list 1 at index {i}")))
for i in range(m):
    l2.append(int(input(f"Enter the element to append in list 2 at index {i}")))
l3=l1+l2
print(l1)
print(l2)
l3.sort()
# print(l3)
l1=[]
l2=[]
for i in range(n):
    l1.append(l3[i])
for i in range(n,n+m):
    l2.append(l3[i])
print(l1)
print(l2)