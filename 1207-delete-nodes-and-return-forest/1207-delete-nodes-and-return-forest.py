# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.forest = []
        self.to_delete = []

    def recur(self, parent_val, node):
        if not node:
            return

        if parent_val in self.to_delete and node.val not in self.to_delete:
            self.forest.append(node)
        
        self.recur(node.val, node.left)
        self.recur(node.val, node.right)

        if node.left and node.left.val in self.to_delete:
            node.left = None
        if node.right and node.right.val in self.to_delete:
            node.right = None

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []

        self.to_delete = to_delete
        if root.val not in self.to_delete:
            self.forest.append(root)
        self.recur(None, root)

        return self.forest