def bestRhombicAreaFrame(matrix, radius):
    maxSum = []
    sub = radius - 1
    for i in range(len(matrix)):
        if i < radius - 1 or len(matrix) - i <= radius-1:
            pass
        else:
            for j in range(len(matrix[i])):
                if j < radius - 1 or len(matrix[i]) - j <= radius-1:
                    pass
                else:
                    try:
                        maxSum.append(matrix[i][j-sub] + matrix[i]
                                      [j+sub] + matrix[i-sub][j] + matrix[i+sub][j])
                    except IndexError:
                        pass
    return sorted(list(set(maxSum)), reverse=True)[:3]


if __name__ == '__main__':
    print(bestRhombicAreaFrame([[3, 5, 2, 1, 4],
                                [4, 1, 4, 5, 3],
                                [6, 2, 7, 2, 1],
                                [10, 0, 4, 2, 7]], 2))
