def performOperations(arr, operations):
    for query in operations:
        if query[0] > 0:
            arr = arr[0:query[0]] + arr[query[1]:query[0]-1:-1] + arr[query[1]+1:]
        else:
            temp = arr[:query[1]]
            temp.reverse()
            arr = temp + arr[query[1]:]

    return set(arr)


if __name__ == '__main__':
    arr = [[0, 1], [1, 3]]
    mylist = list(range(10))
    print(mylist)
    print(performOperations(mylist, arr))
