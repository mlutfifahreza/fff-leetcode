# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def recur(node, prev_max):
            nonlocal res

            if not node:
                return
            
            if prev_max <= node.val:
                res += 1

            prev_max = max(prev_max, node.val)
            
            recur(node.left, prev_max)
            recur(node.right, prev_max)

        recur(root, -1_000_000)

        return res