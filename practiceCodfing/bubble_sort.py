A=[1,5,2,4,3]
for i in range(len(A)):
    # Last i elements are already sorted, so we don't need to compare them again
    for j in range(i,len(A)):
        if A[i] > A[j]:
            # Swap elements if they are in the wrong order
            A[i], A[j] = A[j], A[i]
print(A)