def concatSwaps(s, sizes):
    concatList = [] * len(sizes)
    for i in range(0, len(sizes)):
        if i == 0:
            concatList.append(s[:sizes[i] + 1])
        else:
            concatList.append(s[sizes[i-1]:sizes[i-1] + sizes[i] + 1])

    return ''.join(concatList)


if __name__ == '__main__':
    print(concatSwaps('descognail', [3, 2, 3, 1, 1]))
