class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        res = 0
        multiplier = 0
        while n:
            if not n&1:
                res += pow(2, multiplier)
            multiplier += 1
            n = n >> 1

        return res