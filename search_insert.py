def searchInsert(nums, target):
    length = right = len(nums) - 1
    left = 0

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if mid == length and target > nums[mid]:
        return mid + 1
    if nums[mid] < target and nums[mid+1] > target:
        return mid + 1
    else:
        return mid


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 0))
