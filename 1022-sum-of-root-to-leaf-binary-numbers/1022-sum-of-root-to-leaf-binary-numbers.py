# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def helper(self, node, cursum):
        if not node:
            return
        # print(f'processing node, cursum = {node.val}, {cursum}')
        
        next_cursum = (cursum << 1) + node.val
        if node.left is None and node.right is None:
            # print(f'isleaf true next_cursum = {next_cursum}')
            self.res += next_cursum
        
        self.helper(node.left, next_cursum)
        self.helper(node.right, next_cursum)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.res