l=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS IN THE LIST TO BE STORED :"))
for i in range(n):
    k=int(input(f"Enter the number at index {i}: "))
    l.append(k)
k=0
for i in range(n-1):
    for j in range(i+1, n):
        q=l[i]^l[j]
        if q>k:
            k=q
print("The largest XOR value",k)
    