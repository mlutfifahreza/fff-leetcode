class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums)>1:
            return False

        i = len(nums)-2
        while i > 0:
            if nums[i] != 0:
                i -= 1
            else:
                j = i-1
                while j >= 0:
                    if nums[j] > i-j:
                        i = j
                        break
                    else:
                        j -= 1
                if j < 0:
                    return False
        return i <= 0