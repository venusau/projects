l=[]
li=[]
n=int(input("Enter the length of the array: "))

for i in range(n):
    l.append(int(input(f"Enter the element at the index ({i}): ")))

# print(l)

def frequency(element):
    c=0
    for i in range(n):
        if l[i]==element:
            c=c+1
    return c

for i in range(n):
    if l[i] not in li and frequency(l[i])>1:
        li.append(l[i])

for i in range(len(li)):
    if i<len(li)-1:
        print (li[i], end=",")
    else:
        print(li[i],end="")
               