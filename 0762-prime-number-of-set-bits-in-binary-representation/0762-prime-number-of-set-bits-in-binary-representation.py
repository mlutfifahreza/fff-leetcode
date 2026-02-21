class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 10^6 = 1_000_000
        # 2^10 = 1024
        # 2^20 = > 1mil
        # so max, 20 bits, 0 ... 20
        # prime = 2,3,5,7,11,13,17,19

        def count_bit(n):
            res = 0
            while n > 0:
                res += n % 2
                n >>= 1
            return res
        
        res = 0
        primeset = set([2,3,5,7,11,13,17,19])
        for n in range(left,right+1):
            # print(f'n={n} count_bit(n)={count_bit(n)} check = {count_bit(n) in primeset}')
            if count_bit(n) in primeset:
                res += 1
        return res