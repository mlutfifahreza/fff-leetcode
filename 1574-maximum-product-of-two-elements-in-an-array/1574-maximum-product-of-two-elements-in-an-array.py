class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = nums[0:2]
        if a > b:
            a,b = b,a
        # print(a,b)

        i = 2
        while i < len(nums):
            if nums[i] > b:
                a = b
                b = nums[i]
            elif nums[i] > a:
                a = nums[i]
            # print(a,b)
            i += 1
        return (a-1) * (b-1)