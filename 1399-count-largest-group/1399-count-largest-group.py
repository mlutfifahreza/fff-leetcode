class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digit_count(n):
            res = 0
            while n > 0:
                res += n % 10
                n = n // 10
            return res

        ctr = {}
        for i in range(1, n+1):
            k = digit_count(i)
            if k not in ctr:
                ctr[k] = 0
            ctr[k] += 1
            print(f"{i} -> {k} -> {ctr[k]}")
        
        print(f"ctr = {ctr}")
        
        max_v = 0
        for v in ctr.values():
            if max_v < v :
                max_v = v
        print(f"max_v = {max_v}")
        
        res = 0
        for k,v in ctr.items():
            if v == max_v:
                res += 1
        
        return res