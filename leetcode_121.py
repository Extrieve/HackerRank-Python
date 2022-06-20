class Solution:
    def maxProfit(self, arr: list[int]) -> int:

        ans, left = 0, 0

        for r in range(1, len(arr)):
            if arr[r] < arr[left]:
                left = r

            ans = max(ans, arr[r] - arr[left])

        return ans
