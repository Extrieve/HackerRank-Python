def boundedRatio(a, l, r):
    myBool = [False] * len(a)
    for i in range(1, len(a) + 1):
        if i * l > a[i-1]:
            continue
        elif i * r < a[i-1]:
            continue
        else:
            for j in range(l, r+1):
                if j * i == a[i-1]:
                    myBool[i-1] = True
    return myBool


if __name__ == '__main__':
    print(boundedRatio([1, 2, 3, 4, 5], 2, 10000))
