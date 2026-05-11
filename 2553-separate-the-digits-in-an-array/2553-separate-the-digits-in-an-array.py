class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            temp = []
            while n > 0:
                temp.append(n%10)
                n //= 10
            res.extend(reversed(temp))

        return res