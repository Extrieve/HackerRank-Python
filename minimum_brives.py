def min_brives(q):
    swaps = 0
    og = sorted(q)
    # 1, 0 | 1, 1
    for i, num in enumerate(og):
        moved_index = q.index(num)
        diff = i - moved_index if moved_index < i else 0

        swaps += 1 if i > moved_index else 0

        if diff > 2:
            return 'Too chaotic'
        swaps += diff if diff > 0 else 0

    return str(swaps)


def min_brives1(q):
    swaps = 0
    og = sorted(q)
    # 1, 0 | 1, 1
    for i, num in enumerate(og):
        moved_index = q.index(num)
        
        if i - moved_index > 2:
            return 'Too chaotic'

        if moved_index > i:
            tmp = moved_index - i
            swaps += tmp

    return str(swaps)


def min_brives2(q, n):

    # og = list(range(1, n+1))
    swaps = 0

    for i, x in enumerate(q):
        index = x - 1

        if index - i > 2:
            return 'Too chaotic'

        # tmp = len([x for x in q[:i] if x > q[i]])
        # tpm = 0
        for num in q[:i]:
            if num > x:
                swaps += 1

        # swaps += tpm
    
    return str(swaps)

if __name__ == '__main__':
    arr = [2, 1, 5, 3, 4]
    print(min_brives2(arr, len(arr)))

# 1 2 5 3 7 8 6 4
# 1 2 3 4 5 6 7 8
# 