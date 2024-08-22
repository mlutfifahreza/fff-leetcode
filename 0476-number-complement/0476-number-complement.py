class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        res = 0
        while num > 0:
            if num%2 != 1:
                # print("pow(2, i)", pow(2, i))
                res += pow(2, i)
            num //= 2
            i += 1
        return res