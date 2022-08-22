def less_equal(n, k, arr):
    
    arr.sort()
    candidate = arr[k - 1]
    # arr.insert(k, candidate)
    # print(len([num for num in arr if num <= candidate]))
    return candidate if len([num for num in arr if num <= candidate]) <= k else -1


def less_equal1(n, k, arr):

    arr.sort()
    arr = ''.join(map(str, arr))
    initial = arr[k - 1]
    try:
        index = arr.rindex(initial)
    except ValueError:
        index = k - 1

    return initial if index < k else - 1

    

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(less_equal1(n, k, arr))