# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        helper = ListNode(0, head)
        nums = set(nums)
        # print(f'nums = {nums}')

        prev, cur = helper, head
        while cur:
            # print(f'prev = {prev.val} cur = {cur.val}')
            if cur.val in nums:
                # print(f'removing {cur.val}')
                prev.next = cur.next
                cur = cur.next
            else:
                prev, cur = cur, cur.next
        
        return helper.next