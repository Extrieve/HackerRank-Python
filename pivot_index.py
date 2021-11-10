def practice(nums):
    left, right = 0, sum(nums)

    for i, num in enumerate(nums):
        right -= num
        if right == left:
            return i
        left += num
    return -1


def pivot(nums):
    pivot = len(nums) // 2

    leftSum = sum(nums[pivot:])
    rightSum = sum(nums[:pivot])

    if leftSum > rightSum:
        pivot += 1
        while pivot != len(nums) - 1:
            leftSum = sum(nums[pivot:])
            rightSum = sum(nums[:pivot])
            if rightSum > leftSum:
                return -1
            elif leftSum > rightSum:
                pivot += 1
            else:
                return pivot
    elif rightSum > leftSum:
        pivot -= 1
        while pivot >= 0:
            leftSum = sum(nums[pivot:])
            rightSum = sum(nums[:pivot])
            if leftSum > rightSum:
                return -1
            elif rightSum > leftSum:
                pivot -= 1
            else:
                return pivot
    else:
        return pivot
    return -1


def pivot1(nums):
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1


if __name__ == '__main__':
    print(practice([1, 7, 3, 6, 5, 6]))
