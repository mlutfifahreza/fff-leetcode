# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse right
        right = slow.next
        prev = slow.next = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        # print(head)
        # print(fast)

        left, right = head, prev
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2