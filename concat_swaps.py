def concatSwaps(s, sizes):
    concatList = [''] * len(sizes)
    currentPos = 0
    for i in range(0, len(sizes), 2):
        try:
            print(i, i+1)
            concatList[i] = s[currentPos:sizes[i]+1]
            currentPos += sizes[i]
            concatList[i + 1] = s[currentPos:currentPos + sizes[i+1]]

            concatList[i], concatList[i+1] = concatList[i+1], concatList[i]
        except IndexError:
            concatList[-1] = s[currentPos+sizes[-2]:]
    return ''.join(concatList)


if __name__ == '__main__':
    print(concatSwaps('descognail', [3, 2, 3, 1, 1]))
