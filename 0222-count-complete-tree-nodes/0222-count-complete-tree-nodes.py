# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height_left(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def height_right(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
            
        def countNodesFullBT(h):
            result = 0
            for i in range(h):
                result += pow(2, i)
            return result
        
        def recur(root):
            if not root:
                return 0

            h_left, h_right = height_left(root), height_right(root)
            # print(f"{root.val}, h_left {h_left}, h_right {h_right}")
            if h_left == h_right:
                return countNodesFullBT(h_left)
            else:
                return 1 + recur(root.left) + recur(root.right)

        return recur(root)