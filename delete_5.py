def solution(S):
    # write your code in Python 3.6
    S = [item for item in str(S)]
    newList = S.copy()
    indices = [i for i, x in enumerate(S) if x == '5']
    max = 0
    swap = False
    for item in indices:
        S.pop(item)
        temp = S.copy()
        temp = "".join(temp)
        temp = int(temp)
        if temp > max or swap == False:
            max = temp
            swap = True
        S = newList.copy()
    return max


if __name__ == '__main__':
    print(solution(-5000))
