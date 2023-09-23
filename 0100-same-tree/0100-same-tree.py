# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None):
          return True
        if (p is None or q is None):
          return False
        if p.val != q.val:
          return False
        # look left
        if not self.isSameTree(p.left, q.left):
          return False
        # look right
        if not self.isSameTree(p.right, q.right):
          return False
        # all good
        return True