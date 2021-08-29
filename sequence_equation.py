def permutationEquation(p):
    # Write your code here
    numList = []
    for value in range(1, len(p) + 1):
        index = p.index(p.index(value) + 1)
        numList.append(index + 1)

    return numList


if __name__ == '__main__':
    print(permutationEquation([2, 3, 1]))
