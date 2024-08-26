# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        nums = []
        for ll in lists:
            cur = ll
            while cur:
                nums.append(cur.val)
                cur = cur.next
        # print("nums", nums)

        heapq.heapify(nums)
        # print("nums", nums)

        dummy = ListNode()
        cur = dummy
        while nums:
            v = heapq.heappop(nums)
            node = ListNode(v)
            cur.next = node
            cur = node

        return dummy.next