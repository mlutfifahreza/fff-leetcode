class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse= True)
        # print(f'nums = {nums}')

        res = float('inf')
        for i in range(len(nums)-k+1):
            a,b = nums[i], nums[i+k-1]
            res = min(res, a-b)

        return res