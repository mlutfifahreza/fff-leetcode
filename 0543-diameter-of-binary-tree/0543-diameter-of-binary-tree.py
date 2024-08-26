# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        self.recur(root)
        return self.max_val
    
    def recur(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        l,r = self.recur(node.left), self.recur(node.right)
        
        self.max_val = max(self.max_val, l+r)
        return max(l,r) + 1