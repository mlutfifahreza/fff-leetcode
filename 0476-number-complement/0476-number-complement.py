class Solution:
    def findComplement(self, num: int) -> int:
        # i = 0
        # res = 0
        # while num > 0:
        #     if num%2 == 0:
        #         res += pow(2, i)
        #     num //= 2
        #     i += 1
        # return res

        res = 0
        for i in range(40):
            if num < 1:
                break
            
            if num % 2 == 0:
                res += pow(2, i)
            
            num //= 2
        
        return res