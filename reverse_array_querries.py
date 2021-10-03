def performOperations(arr, operations):
    newArr = []
    for item in operations:
        print(arr[item[0]:item[1]+1])
        newArr += arr[item[0]:item[1]:-1]
    return newArr


if __name__ == '__main__':
    arr = [[0, 1], [1, 3]]
    print(performOperations([5, 3, 2, 1, 3], arr))
