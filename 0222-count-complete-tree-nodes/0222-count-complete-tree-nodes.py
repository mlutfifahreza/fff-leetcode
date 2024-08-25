# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate the height of the leftmost path
        def height_left(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        # Helper function to calculate the height of the rightmost path
        def height_right(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        # Main recursive function to count nodes
        def recur(node):
            if not node:
                # Base case: if the node is None, return 0
                return 0

            # Calculate the height of the leftmost and rightmost paths
            h_left = height_left(node)
            h_right = height_right(node)
            
            if h_left == h_right:
                # If the left and right heights are equal, the tree is a perfect binary tree
                # The number of nodes in a perfect binary tree of height h is 2^h - 1
                return pow(2,h_left) - 1
            else:
                # If the heights are different, recursively count the nodes in the left and right subtrees
                return 1 + recur(node.left) + recur(node.right)

        # Start the recursion from the root
        return recur(root)
