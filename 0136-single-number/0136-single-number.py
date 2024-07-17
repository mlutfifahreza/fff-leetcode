class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            if n in d:
                d.pop(n)
            else:
                d[n] = True
        return list(d.keys())[0]