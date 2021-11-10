import collections


def deleteAndEarn(nums):
    while nums:
        frequencies = dict()
        for item in nums:
            if item not in frequencies:
                frequencies[item] = 1
            else:
                frequencies[item] += 1

        points = []

        for item in frequencies.items():
            points.append((item[0], item[0] * item[1]))

        sorted(points, key=lambda k: k[1])


def dynamicDeleteEarn(nums):
    count = collections.Counter(nums)
    prev = None
    avoid = using = 0
    for k in sorted(count):
        if k - 1 != prev:
            avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
        else:
            avoid, using = max(avoid, using), k * count[k] + avoid
        prev = k
    return max(avoid, using)


if __name__ == '__main__':
    print(dynamicDeleteEarn([3, 4, 2]))
