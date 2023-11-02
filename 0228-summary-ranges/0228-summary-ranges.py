class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        last_index = len(nums) - 1
        if last_index == -1:
            return []
        
        result = []
        start_end = [nums[0], None]
        for i in range(len(nums)):
            if nums[i] - nums[i-1] > 1:
                start_end[1] = nums[i-1]
                if start_end[1] == start_end[0]:
                    result.append(f"{start_end[0]}")
                else:
                    result.append(f"{start_end[0]}->{start_end[1]}")
                start_end[0] = nums[i]
            if i == last_index:
                start_end[1] = nums[i]
                if start_end[1] == start_end[0]:
                    result.append(f"{start_end[0]}")
                else:
                    result.append(f"{start_end[0]}->{start_end[1]}")
        return result