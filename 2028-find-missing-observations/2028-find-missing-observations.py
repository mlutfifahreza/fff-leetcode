class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean*(len(rolls)+n) - sum(rolls)
        
        if target / n > 6 :
            return []
        
        if target < n:
            return []
        
        avg_target = target//n
        res = [avg_target] * n

        target = target - avg_target*n

        for i in range(target):
            res[i] += 1
        
        return res