class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        num_sum = 0
        inf_float = float('inf')
        res = inf_float

        while r < len(nums):
            num_sum += nums[r]

            while (num_sum >= target):
                res = min(res, r-l+1)
                num_sum -= nums[l]
                l += 1
            
            r += 1
        
        return res if res != inf_float else 0