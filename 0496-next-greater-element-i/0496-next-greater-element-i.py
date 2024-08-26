class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_next = {}

        stack = []

        for n in nums2:
            # print()
            # print("stack", stack)
            while stack and stack[-1] < n:
                k = stack.pop()
                # print("pop", k)
                val_next[k] = n
            stack.append(n)
        
        # print("stack", stack)
        # print("val_next", val_next)

        res = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            if n in val_next:
                res[i] = val_next[n]

        return res