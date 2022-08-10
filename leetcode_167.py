class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers)
        start, end = 0, length - 1
        
        while start != end:
            cur = numbers[end] + numbers[start]
            
            if cur == target:
                return [start+1, end+1]
            
            if cur < target:
                start += 1
            else:
                end -= 1
            
        return [start+1, end+1]