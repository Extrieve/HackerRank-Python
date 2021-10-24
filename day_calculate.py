def solution(S, K):
    # write your code in Python 3.6
    days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    index = days.index(S)
    return days[(index+K) % 7]


if __name__ == '__main__':
    print(solution('Wed', 2))
