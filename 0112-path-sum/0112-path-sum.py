# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumWithSum(self, node, targetSum, currSum):
        if node is None:
            return False
        if node.left is None and node.right is None:
            # print(f"{currSum} == {targetSum} is {currSum == targetSum}")
            return currSum + node.val == targetSum
        # print(f"{currSum} + {node.val}")
        currSum += node.val
        return self.hasPathSumWithSum(node.left, targetSum, currSum) or self.hasPathSumWithSum(node.right, targetSum, currSum)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        return self.hasPathSumWithSum(root, targetSum, 0)