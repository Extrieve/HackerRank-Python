def sub_sort(arr):
    arr = sorted(arr, key=lambda x: len(x))
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] in arr[j]:
                continue
            return ['NO']

    arr.insert(0, 'YES')
    return arr


if __name__ == '__main__':

    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input())

    print('\n'.join(sub_sort(arr)))