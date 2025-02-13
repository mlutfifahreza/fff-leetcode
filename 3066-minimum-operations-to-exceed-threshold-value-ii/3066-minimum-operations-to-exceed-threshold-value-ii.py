class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = []
        [heappush(h,n) for n in nums if n < k]

        res = 0
        while len(h)>1:
            a,b = heappop(h), heappop(h)
            new_val = a * 2 + b
            if new_val < k:
                heappush(h, new_val)
            res += 1
        
        return res + len(h)