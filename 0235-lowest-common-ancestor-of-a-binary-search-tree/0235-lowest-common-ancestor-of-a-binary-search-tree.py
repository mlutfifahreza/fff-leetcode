# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a, b = p.val, q.val
        if a > b:
            b, a = a, b

        return self.recur(root, a, b)
    
    def recur(self, node, a, b):
        # print(node.val, a, b)
        if node.val > b:
            return self.recur(node.left, a, b)
        elif node.val < a:
            return self.recur(node.right, a, b)
        else:
            return node