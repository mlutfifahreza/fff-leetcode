class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        from collections import deque
        dq = deque()

        res = []
        n = len(nums)
        for i in range(n):
            val = nums[i]
            # remove unusable
            if i >= k:
                v = nums[i-k]
                if dq[0] == v:
                    dq.popleft()

            # remove if dq last < n
            while dq and dq[-1] < val:
                dq.pop()

            # append n
            dq.append(val)

            if i >= k-1:
                res.append(dq[0])
        
        return res