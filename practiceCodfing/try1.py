def sort_list(l):
    for i in range(len(l)):
        for j in range(i,len(l)-1):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l
l = [[1, 2, 3, 4], [5, 6, 4, 7], [1, 2, 9]]

for i in range(len(l)):
    for j in range(len(l[i])):
        for k in range(len(l[i]) - 1):
            if l[i][k] > l[i][k + 1]:
                l[i][k], l[i][k + 1] = l[i][k + 1], l[i][k]
k=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        k.append(l[i][j])
k=sort_list(k)
print(k)