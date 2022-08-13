class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length - 1
        
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1