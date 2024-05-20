l=[]
mylist=[]
n=int(input("Enter the lengtht of the array : "))

for i in range(n):
    l.append(int(input(f"Enter the element at the index ({i}): ")))

for i in range(n):
    product=1
    for j in range(n):
        if not l[i]==l[j]:
            product=product*l[j]

    mylist.append(product)
    print(f"Product of the elements except {l[i]} is: {product}")
