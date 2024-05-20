l=[]
n=int(input("Enter the length of the list : "))

for i in range(n):
    l.append(int(input(f"Enter the element to be appended at the index ({i}): ")))

def checking(l):
    check=[False,0]
    k=int(input("Enter the key to be searched in the list : "))
    for i in range(n):
        if k==l[i]:
            check[0]=True
            check[1]=i
            break
        
    return check

k=checking(l)
# print(k)
if k[0]==True and not k[1]==0:
    print(f"Found at the index {k[1]}")
else:
    print("Not found")