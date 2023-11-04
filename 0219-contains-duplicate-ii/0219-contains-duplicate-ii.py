class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # len_num = len(nums)
        # for i in range(len_num-1):
        #     j = i + 1
        #     max_j = i+k
        #     while (j<len_num and j<=max_j):
        #         if nums[i] == nums[j]:
        #             return True
        #         j += 1
        # return False

        indexes = {}
        for i in range(len(nums)):
            val = nums[i]
            if val not in indexes:
                indexes[val] = i
            else:
                if i - indexes[val] <= k:
                    # print(f"True at i={i} val={val} last_index={indexes[val]}")
                    return True
                else:
                    indexes[val] = i
        
        return False