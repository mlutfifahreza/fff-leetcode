class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean*(len(rolls)+n) - sum(rolls)
        # print(f'target = {target}')
        
        if target / n > 6 :
            return []
        
        if target < n:
            return []
        
        res = [0] * n

        for i in range(n):
            rest = n-i-1
            for v in range(6, 0 ,-1):
                if target - v >= rest:
                    res[i] = v
                    target -= v
                    break
        
        return res