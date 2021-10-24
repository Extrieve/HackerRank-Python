def solution(A):
    # write your code in Python 3.6
    A = sorted(A, reverse=False)
    for item in A:
        if item + 1 not in A and item > 0:
            return item + 1
    return 1


if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))
