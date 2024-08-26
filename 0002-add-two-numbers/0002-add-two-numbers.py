# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        hold = 0
        while l1 or l2 or hold:
            new_val = hold
            if l1: 
                new_val += l1.val
                l1 = l1.next
            if l2:
                new_val += l2.val
                l2 = l2.next
            hold = new_val // 10
            new_val = new_val % 10
            cur.next = ListNode(new_val)
            cur = cur.next
        
        return dummy.next