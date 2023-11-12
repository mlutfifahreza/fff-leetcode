# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:        
        global total_sum
        def add_root_to_leaf(node, curr_num):
            if node == None:
                return
            elif node.left == None and node.right == None:
                global total_sum
                total_sum += (curr_num*10)+node.val
            else:
                curr_num = (curr_num*10)+node.val
                add_root_to_leaf(node.left, curr_num)
                add_root_to_leaf(node.right, curr_num)
        
        total_sum = 0
        add_root_to_leaf(root, 0)
        
        return total_sum