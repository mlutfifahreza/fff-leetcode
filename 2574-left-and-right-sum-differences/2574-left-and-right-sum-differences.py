class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = []
        lc = 0
        rsum = []
        rc = 0
        max_idx = len(nums) - 1

        for i,n in enumerate(nums):
            # print('process', i,n)
            lsum.append(lc)
            lc += n
            rsum.insert(0, rc)
            rc += nums[max_idx-i]
        
        # print(lsum, rsum)

        for i,n in enumerate(lsum):
            lsum[i] = abs(n - rsum[i])
        
        # print(lsum)

        return lsum