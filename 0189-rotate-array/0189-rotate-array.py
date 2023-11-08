class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_num = len(nums)
        if k == 0 or k == len_num or len_num == 1:
            return

        len_num = len_num
        shift = k % len_num
        a = nums[len_num-shift:len_num] if len_num-shift < len_num else []
        # print(a)
        b = nums[:len_num-shift]
        # print(b)

        i = 0
        while i < len(a):
            nums[i] = a[i]
            i += 1
        j = 0
        while j < len(b):
            nums[i+j] = b[j]
            j += 1
        # print(nums)