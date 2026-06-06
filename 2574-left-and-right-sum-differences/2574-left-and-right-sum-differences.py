class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        ans = []
        
        for num in nums:
            # Right sum for the current element excludes the element itself
            right_sum -= num 
            
            ans.append(abs(left_sum - right_sum))
            
            # Left sum for the NEXT element includes the current element
            left_sum += num
            
        return ans