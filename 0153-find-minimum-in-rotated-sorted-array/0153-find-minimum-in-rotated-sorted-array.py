class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        return self.bs(nums)
        
    def bs(self, li):
        if len(li) <= 2:
            return min(li)
        
        mid = len(li) // 2
        if li[mid] < li[0]:
            return self.bs(li[:mid+1])
        else:
            return self.bs(li[mid:])