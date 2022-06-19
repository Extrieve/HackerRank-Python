import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = string.ascii_lowercase + string.digits
        s = ''.join([c for c in s.lower() if c in valid])

        return s == s[::-1]