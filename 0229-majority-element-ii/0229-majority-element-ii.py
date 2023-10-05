class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_count = int(len(nums) // 3)
        count_d = {}
        for n in nums:
            if n not in count_d:
                count_d[n] = 0
            count_d[n] += 1
        res = []
        for k,v in count_d.items():
            if v > min_count:
                res.append(k)
        return res