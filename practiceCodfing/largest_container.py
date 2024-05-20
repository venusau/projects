def append_list(l,i):
    l.append(int(input(f"enter the element to be appended at l({i}) : ")))
k=1
l=[]
i=0
while k==1:
    append_list(l,i)
    i+=1
    k=int(input("Keep entering 1 to append the list :"))
