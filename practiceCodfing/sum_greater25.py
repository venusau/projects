n=int(input("Enter the number of elements to inserted in the list : "))
l=[]
for i in range (n):
    l.append(int(input(f"Enter the number at positon l({i}): ")))
for i in range(n-1):
    for j in range(i+1,n,1):
        s=l[i]+l[j]
        if s==25:
            print(f"[{l[i]},{l[j]}]")