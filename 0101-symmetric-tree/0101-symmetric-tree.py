# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricLeftRight(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return left.val == right.val and self.isSymmetricLeftRight(left.left, right.right) and self.isSymmetricLeftRight(left.right, right.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.isSymmetricLeftRight(root.left, root.right)