def judges_scores(judges, rated):
    if rated == 0:
        return "-3.0 3.0"
    else:
        scoreCumulation = 0
        for i in range(rated):
            scoreCumulation += float(input())

        if rated == judges:
            scoreCumulation /= rated
            return f"{scoreCumulation} {scoreCumulation}"
        else:
            remainingJudges = judges - rated
            minPossible = (scoreCumulation + (-3 * remainingJudges)) / judges
            maxPossible = (scoreCumulation + (3 * remainingJudges)) / judges
            return f"{minPossible} {maxPossible}"


if __name__ == '__main__':
    x = input()
    x = [int(i) for i in x.split()]
    print(judges_scores(x[0], x[1]))
