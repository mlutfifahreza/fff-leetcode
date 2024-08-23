# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return [], 0
            # leaf
            elif node.left is None and node.right is None:
                # print("find a leave", node.val)
                return [1], 0
            else:
                l, res_l = dfs(node.left)
                r, res_r = dfs(node.right)
                # print("not a leaf", l, r)
                res = res_l + res_r
                for v1 in l:
                    for v2 in r:
                        if v1 + v2 <= distance:
                            res += 1
                return ([v+1 for v in l] + [v+1 for v in r]), res
        
        li, res = dfs(root)
        # print("li", li)
        # print("res", res)
        
        return res