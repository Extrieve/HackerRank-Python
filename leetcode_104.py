# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: any[TreeNode], maxD = 0) -> int:
        
        if not root:
            return maxD
    
        return max(self.maxDepth(root.right, maxD+1), self.maxDepth(root.left, maxD+1))
        
        
        