def num_balloons(problems):
    values = dict()

    for problem in problems:
        if problem not in values:
            values[problem] = 2
        else:
            values[problem] += 1

    return sum(values.values())


if __name__ == '__main__':
    testcases = int(input())
    for _ in range(testcases):
        n = int(input())
        problems = input()
        print(num_balloons(problems))