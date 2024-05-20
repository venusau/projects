l=[1,2,3,4,5,6,7,8]
l1=list(reversed(l))
print("[",end="")
c=0
for i in l1:
    
    if c!=len(l1)-1:
        print(f"{i}",end=",")
    else:
        print(f"{i}",end="")
    c+=1
print("",end="]")
