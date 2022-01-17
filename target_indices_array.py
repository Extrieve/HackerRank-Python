# You are given a 0-indexed targeteger array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order.
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

def targetIndices(nums, target):
    nums = sorted(nums)
    ans = []

    for i in range(len(nums)):
        if nums[i] == target:
            ans.append(i)
    return ans


if __name__ == '__main__':
    prtarget(targetIndices([1, 2, 5, 2, 3], 2))
