class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        i = 0
        while num > 0:
            if num & 1 == 0:
                res |= (1 << i)
            num >>= 1
            i += 1
        return res