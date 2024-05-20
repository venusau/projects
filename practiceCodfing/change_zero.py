def change_zero(l, i, j, n, m):
    for a in range(n):
        l[i][a] = 0
    for a in range(m):
        l[a][j] = 0

def check_zero(l):
    m = len(l)
    n = len(l[0])
    zero_rows = set()
    zero_cols = set()
    
    # Find the indices of rows and columns containing zeroes
    for i in range(m):
        for j in range(n):
            if l[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    # Set entire rows to 0 based on the indices found
    for i in zero_rows:
        for j in range(n):
            l[i][j] = 0
    
    # Set entire columns to 0 based on the indices found
    for j in zero_cols:
        for i in range(m):
            l[i][j] = 0

# Input matrix
matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

check_zero(matrix)
print(matrix)
