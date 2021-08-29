import itertools
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#


def acmTeam(topic):
    # Write your code here
    nmT = 0
    cnt = 0
    for i in itertools.combinations(topic, 2):
        s = bin(int(i[0], 2) | int(i[1], 2)).count('1')
        if nmT < s:
            nmT = s
            cnt = 0
        if s == nmT:
            cnt += 1
    return (nmT, cnt)


def acmTeam1(topic):
    # Write your code here
    combinations = itertools.combinations(
        (x for x in range(1, len(topic) + 1)), 2)

    max = 0
    count = 0
    for teams in combinations:
        current = 0
        for i in range(len(topic[0])):
            print(i)
            if topic[teams[0]-1][i] == '1' or topic[teams[1]-1][i] == '1':
                #print(topic[teams[0]-1][0] or topic[teams[1]-1][0] == '1')
                current += 1
        if current == max:
            count += 1
        elif current > max:
            max = current
            count = 1

    return [max, count]


if __name__ == '__main__':
    print(acmTeam(['10101', '11110', '00010']))
