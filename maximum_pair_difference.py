import itertools
from math import prod


def maxProductDifference(nums):
    combinations = list(itertools.combinations(nums, 2))
    productCombinations = [prod(item) for item in combinations]
    return (max(productCombinations) - min(productCombinations))


def maxProductDifference2(nums):
    newlist = sorted(nums)
    top = prod(newlist[len(nums)-2:len(nums)])
    bottom = prod(newlist[:2])

    return top - bottom


print(maxProductDifference([5, 6, 2, 7, 4]))

print(maxProductDifference2([5, 6, 2, 7, 4]))
