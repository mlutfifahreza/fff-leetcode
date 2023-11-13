class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = sorted(nums)
        # # print("sort", nums)
        # keys = set()
        # res = []
        # for i in range(0, len(nums)-2):
        #     if nums[i] > 0:
        #         continue
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             a,b,c = nums[i], nums[j], nums[k]
        #             if a+b+c == 0:
        #                 key = str((a,b,c))
        #                 if key not in keys:
        #                     res.append([a,b,c])
        #                     keys.add(key)
        # return res
        
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, len(nums)-1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    last_low = nums[j]
                    while j<k and nums[j] == last_low:
                        j += 1
                    
                    last_high = nums[k]
                    while j<k and nums[k] == last_high:
                        k -= 1

        return res