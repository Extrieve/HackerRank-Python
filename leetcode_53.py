class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        mymax = nums[0]
        tmp = mymax
        for n in nums[1:]:
            
            if tmp + n < n and n > tmp:
                tmp = n
            else:
                tmp += n
            
            mymax = max(tmp, mymax)
        return mymax