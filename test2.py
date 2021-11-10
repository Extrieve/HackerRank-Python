mymatrix = [[1, 2, 3], [4, 5, 6]]

col_unique = dict()
for i in range(len(mymatrix)):
    for j in range(len(mymatrix[0])):
        if j in col_unique:
            col_unique[j] = mymatrix[i][j]
