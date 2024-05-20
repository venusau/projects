l=[1,-1,0,2,-1,2,4]
l.sort()
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            sum=l[i]+l[j]+l[k]
            if sum==0:
                print(f"[{l[i]},{l[j]},{l[k]}]")



