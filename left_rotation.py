def rotLeft(a, rotations):
    return a[rotations:] + a[:rotations]


if __name__ == '__main__':
    n, rotations = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(rotLeft(arr, rotations % n))