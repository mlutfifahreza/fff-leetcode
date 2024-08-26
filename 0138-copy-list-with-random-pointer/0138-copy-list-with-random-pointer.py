"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None: None}

        node = head
        while node:
            new_node = Node(node.val)
            old_to_copy[node] = new_node
            node = node.next
        
        node = head
        while node:
            copy = old_to_copy[node]
            copy.next = old_to_copy[node.next]
            copy.random = old_to_copy[node.random]
            node = node.next
         
        return old_to_copy[head]