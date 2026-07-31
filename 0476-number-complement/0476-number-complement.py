class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        counter = 0
        while num > 0:
            temp = num & 1
            if temp == 0:
                res += pow(2,counter)
            num = num >> 1
            counter += 1
        
        return res