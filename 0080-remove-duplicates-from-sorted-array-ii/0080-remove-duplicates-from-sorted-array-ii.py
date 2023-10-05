class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        alr_two = False
        last_num = -12312312
        max_index = len(nums) - 1
        i = 0
        while i <= max_index:
            n = nums[i]
            if n == last_num:
                if alr_two:
                    nums.pop(i)
                    max_index -= 1
                    continue
                else:
                    alr_two = True
            else:
                alr_two = False
                last_num = n
            i += 1
        return len(nums)