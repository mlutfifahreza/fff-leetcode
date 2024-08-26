"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def recur(node):
            if not node:
                return
            # print(node.val)
            if node.children:
                for c in node.children:
                    recur(c)
            
            res.append(node.val)
        
        recur(root)
        
        return res