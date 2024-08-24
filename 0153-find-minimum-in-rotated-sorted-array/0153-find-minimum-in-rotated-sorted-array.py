class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]
        
        if len(nums) <= 2:
            return min(nums)
        
        mid = len(nums) // 2
        # print("nums, mid", nums, mid)
        if nums[mid] < nums[0]:
            return self.findMin(nums[:mid+1])
        else:
            return self.findMin(nums[mid+1:])