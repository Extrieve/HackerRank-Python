import itertools


def oddSublist(arr):
    if(sum(arr) % 2 != 0):
        return sum(arr)
    else:
        return 0


def sumOddLengthSubarrays(arr):
    oddSubs = []
    for i in range(0, len(arr), 2):
        combinations = list(itertools.permutations(arr, i+1))
        for item in combinations:
            if(len(item) % 2 != 0):
                #print(item, sum(item))
                oddSubs.append(sum(item))

    return sum(oddSubs)


def sumOddLengthSubarrays2(arr):
    oddSubs = []
    for i in range(0, len(arr) + 1):
        for j in range(i):
            if(len(arr[j: i]) % 2 != 0):
                print(arr[j: i])
                oddSubs.append(sum(arr[j: i]))

    return sum(oddSubs)


if __name__ == '__main__':
    print(sumOddLengthSubarrays2([1, 4, 2, 5, 3]))
