# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(node):
            if not node:
                return 0, True
            if not node.left and not node.right:
                return 1, True
            l,bl = recur(node.left)
            r,br = recur(node.right)

            if not bl or not br:
                return 0, False
            
            if abs(l-r) > 1:
                return 0, False
            
            return max(l,r) + 1, True
            
        _, b = recur(root)
        return b