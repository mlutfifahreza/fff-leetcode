class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        res = 0

        prefix = 0
        for n in nums:
            prefix += n
            key = prefix % k
            if key in dic:
                res += dic[key]
                dic[key] += 1
            else:
                dic[key] = 1
        
        return res