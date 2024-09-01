# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(node, min_val, max_val):
            if not node:
                return True
            
            if not(min_val < node.val < max_val):
                return False
            
            left = recur(node.left, min_val, node.val)
            right = recur(node.right, node.val, max_val)

            return left and right
        
        return recur(root, -float('inf'), float('inf'))