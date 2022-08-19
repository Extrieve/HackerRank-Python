class Solution:
    def isValid(self, s: str) -> bool:
        myset = {'()', '[]', '{}'}
        stack = []
        for c in s:
            stack.append(c)
            while True:
                try:
                    print(stack[-2] + stack[-1])
                    if stack[-2] + stack[-1] in myset:
                        stack.pop()
                        stack.pop()
                    else:
                        break
                except IndexError:
                    break
                        
        return True if not stack else False
