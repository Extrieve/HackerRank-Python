class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = dict()
        
        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1
        
        output = [i for i, x in sorted(ans.items(), key=lambda x: x[1], reverse=True)]
        return output[:k]