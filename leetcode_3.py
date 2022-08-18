class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        ss = ""
        maxLength = 0
        for c in string:
            lastIndex = ss.find(c)
            if lastIndex > -1:
                ss = ss[lastIndex + 1:]
            ss += c
            maxLength = max(maxLength, len(ss))
        return maxLength