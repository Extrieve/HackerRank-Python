def minSubArrayLen(s, nums):
    total = left = 0
    result = len(nums) + 1
    for right, n in enumerate(nums):
        total += n
        print(total)
        while total >= s:
            #print(result)
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
            #print(result, left)
    return result if result <= len(nums) else 0

if __name__ == '__main__':
    print(minSubArrayLen(7, [2,3,1,2,4,3]))
