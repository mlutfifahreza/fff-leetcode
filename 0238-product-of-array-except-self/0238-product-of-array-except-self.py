class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        su = 1
        for i in range(n-1):
            su *= nums[i]
            res[i+1] = su
        
        su = 1
        for i in range(n-1, 0, -1):
            su *= nums[i]
            res[i-1] *= su
        
        return res