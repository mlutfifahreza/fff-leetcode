# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def recur(node, counter):
            if not node:
                return None, counter
            
            # check left
            found, counter = recur(node.left, counter)
            if found is not None:
                return found, counter
            # check curr
            counter += 1
            if counter == k:
                return node.val, counter
            # check right
            found, counter = recur(node.right, counter)
            return found, counter
        
        found, _ = recur(root, 0)
        return found