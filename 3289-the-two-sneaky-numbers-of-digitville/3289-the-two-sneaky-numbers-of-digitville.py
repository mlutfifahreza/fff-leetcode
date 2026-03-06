class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        found_set = set()
        res = []

        for n in nums:
            if n in found_set:
                res.append(n)
            else:
                found_set.add(n)
        
        return res