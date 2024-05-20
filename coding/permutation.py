from itertools import permutations 
def permute(l):
    return list(permutations(l))
l=[1,2,3]
k=permute(l)
print(k)