l=[]

n=int(input("Enter the length of the list : "))

for i in range (n):
    l.append(int(input(f"Enter the element at the index of ({i}): ")))

max_product=0
for i in range(n-1):
    product=l[i]
    if i==0:
        k=n-1
    else:
        k=n
    while k>i+1:
        for j in range(i+1,k):
            # print(j)
            if product*l[j]>product:
                product=product*l[j]
                print(product)
            # else:
            #     break
                
        k=k-1
            

    if product>max_product:
        max_product=product
 
print(f"The max product is the {max_product}")
    