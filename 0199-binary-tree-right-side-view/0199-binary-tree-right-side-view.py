# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recur(node, level):
            if not node:
                return

            if len(res) == level:
                res.append(0)
            
            # print(f'recur({node.val}, {level}) | res = {res}')
            
            res[level] = node.val
            recur(node.left, level + 1)
            recur(node.right, level + 1)
        
        recur(root, 0)

        return res