def binary_search(nums, target):
    if len(nums) <= 1 and nums[0] != target:
        return False

    mid = len(nums)//2
    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binary_search(nums[mid:], target)
    elif nums[mid] > target:
        return binary_search(nums[mid:], target)


def indexed_binarySearch(nums, target):
    arr_length = len(nums)
    left = 0
    right = arr_length - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(indexed_binarySearch([-1, 0, 3, 5, 9, 12], 9))
