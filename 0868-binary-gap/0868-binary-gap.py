class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        cur = 0

        while n % 2 == 0:
            n >>= 1

        while n > 0:
            if n % 2 == 1:
                res = max(res, cur)
                cur = 1
            else:
                cur += 1
            n >>= 1
        
        return res