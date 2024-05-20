l=[]
n=int(input("Enter the length of the list : "))

for i in range(n):
    l.append(int(input(f"Enter the element at the index({i}): ")))
l.sort()
m=int(input("Enter the number of students : "))
ultimate_list=[]
for i in range(n):
    temp_list=[]
    for j in range(i,m+i):
        if j>=n:
            break
        temp_list.append(l[j])
    if len(temp_list)==m:
        ultimate_list.append(temp_list)
    else:
        break
# print(len(ultimate_list))
k=float('inf')
print("[",end="")
for i in range(len(ultimate_list)):
    temp_list=ultimate_list[i]
    if not temp_list[m-1]-temp_list[0]>k:
        k=temp_list[m-1]-temp_list[0]
        if not i==len(ultimate_list)-1:
            print(k,end=",")
        else:
            print(k,end="")
print("]")  
print(k)
    