# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge_two_list(list_1, list_2):
            if not list_1:
                return list_2
            if not list_2:
                return list_1
                
            dummy = ListNode()
            curr = dummy
            while list_1 and list_2:
                if list_1.val < list_2.val:
                    curr.next = list_1
                    list_1 = list_1.next
                else:
                    curr.next = list_2
                    list_2 = list_2.next
                curr = curr.next
            
            while list_1:
                curr.next = list_1
                list_1 = list_1.next
                curr = curr.next

            while list_2:
                curr.next = list_2
                list_2 = list_2.next
                curr = curr.next
            
            return dummy.next

        while len(lists) > 1:
            merge_lists = []
            for i in range(len(lists)):
                if i % 2 == 1:
                    res = merge_two_list(lists[i-1], lists[i])
                    merge_lists.append(res)
            
            if len(lists) % 2 == 1:
                merge_lists.append(lists[-1])
            
            lists = merge_lists

        
        return lists[0]