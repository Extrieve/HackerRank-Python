class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = prices[0]
        total = 0
        for right in prices:
            if right < left:
                left = right
            else:
                total += right - left
                left = right
                
        return total