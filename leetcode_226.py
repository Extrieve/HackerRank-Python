class Solution:
    def invertTree(self, root: any[TreeNode]) -> any[TreeNode]:
        
        if not root:
            return root
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root