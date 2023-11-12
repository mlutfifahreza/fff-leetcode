class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_len = 1
        curr_len = 1
        nums = sorted(nums)
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            elif nums[i] - nums[i-1] == 1:
                curr_len += 1
            else:
                if curr_len > max_len: max_len = curr_len
                curr_len = 1
        if curr_len > max_len: max_len = curr_len

        return max_len