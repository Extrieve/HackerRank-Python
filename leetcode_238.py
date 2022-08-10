import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = math.prod(nums)
        ans = []
        for i, n in enumerate(nums):
            cur  = prod
            if n != 0:
                ans.append(cur//n)
            else:
                # print(nums[:i], nums[i+1:])
                cur = math.prod(nums[:i] + nums[i+1:])
                ans.append(cur)
                
        return ans