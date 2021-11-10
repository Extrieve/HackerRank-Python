def numTeams(rating):
    teams = []
    for i in range(len(rating)):
        for j in range(i+1, len(rating)):
            for k in range(j+1, len(rating)):
                if (rating[k] > rating[j] > rating[i]) or (rating[k] < rating[j] < rating[i]):
                    teams.append([rating[i], rating[j], rating[k]])
    return len(teams)


def numTeams1(rating):
    asc = dsc = 0
    for i, v in enumerate(rating):
        llc = rgc = lgc = rlc = 0
        for l in rating[:i]:
            if l < v:
                llc += 1
            if l > v:
                lgc += 1
        for r in rating[i+1:]:
            if r > v:
                rgc += 1
            if r < v:
                rlc += 1
        asc += llc * rgc
        dsc += lgc * rlc
    return asc + dsc


if __name__ == '__main__':
    print(numTeams1([1, 2, 3, 4]))
