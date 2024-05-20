n=int(input("Enter the number of elements you wanna put in the list :"))
l=[]
for i in range(n):
    l.append(int(input(f"enter number at position l({i}): ")))
i=1
while True:
    if i in l:
        i+=1
        continue 
    else:
        break
print(f"The smallest positive number that is not present in the list is {i}")