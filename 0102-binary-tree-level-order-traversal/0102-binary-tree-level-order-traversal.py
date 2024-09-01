# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def recur(node, level, res):
            if not node:
                return
            # print("node.val", node.val, "level", level, "res", res)
            recur(node.left, level+1, res)
            res[level].append(node.val)
            recur(node.right, level+1, res)
        
        recur(root, 0, res)
        # print("res", res)

        res_list = []
        for _ in range(len(res)):
            res_list.append([])
        for level, val in res.items():
            res_list[level] = val

        # print("res_list", res_list)
        return res_list