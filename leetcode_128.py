class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()
        mymax, tmp = 1, 1
        for i, n in enumerate(nums):
            if i == 0:
                pass
            
            prev = nums[i-1]
            if n-1 == prev:
                tmp += 1
                if tmp > mymax: 
                    mymax = tmp
            elif n == prev:
                pass
            else:
                tmp = 1
                if tmp > mymax:
                    mymax = tmp
        
        return mymax 