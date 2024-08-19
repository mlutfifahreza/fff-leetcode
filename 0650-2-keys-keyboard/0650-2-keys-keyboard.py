class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        while n > 1:
            i = 2
            while n%i != 0:
                i += 1
            result += i-1 # pase
            result += 1 # copy
            n = n/i
        
        return result