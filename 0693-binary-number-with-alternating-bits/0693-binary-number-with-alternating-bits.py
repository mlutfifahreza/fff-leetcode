class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n % 2
        n //= 2
        
        while n > 0:
            x = n % 2
            if x == last:
                return False
            last = x
            n //= 2
        
        return True