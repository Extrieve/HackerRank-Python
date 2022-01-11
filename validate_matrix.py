def validate_matrix(matrix):
    valid = True
    cols_val = [dict()] * len(matrix[0])
    for i in range(len(matrix)):
        mydict = dict()
        for j in range(len(matrix[0])):

            if matrix[i][j] not in cols_val[j]:
                cols_val[i][matrix[i][j]] = 1
            else:
                valid = False
                print(cols_val, f'\nRepeated Value: {matrix[i][j]}')
                return valid

            if matrix[i][j] not in mydict:
                mydict[matrix[i][j]] = 1
            else:
                valid = False
                print(cols_val, f'\nRepeated Value: {matrix[i][j]}')
                return valid

    print(cols_val)
    return valid


if __name__ == '__main__':
    mymatrix = [
        [1, 2, 3],
        [4, 5, 6],
        [1, 3, 4]
    ]
    print(validate_matrix(mymatrix))
