def contestants(scoresArray):
    maxScore = 0
    indexContestant = 0
    for i in range(len(scoresArray)):
        if sum(scoresArray[i]) > maxScore:
            maxScore = sum(scoresArray[i])
            indexContestant = i

    return f'{indexContestant + 1} {maxScore}'


if __name__ == '__main__':
    testcase = []
    for i in range(5):
        x = input()
        x = [int(i) for i in x.split()]
        testcase.append(x)
    print(contestants(testcase))
