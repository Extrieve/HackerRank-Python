class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        candidate = strs[0]
        build = ""
        for i, s in enumerate(candidate):
            for sc in strs[1:]:
                if not sc.startswith(candidate[:i+1]):
                    return build
            build += s
        
        return build