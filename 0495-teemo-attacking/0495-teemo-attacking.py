class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        exp = -1

        for t in timeSeries:
            new_exp = t+duration-1
            res += min(new_exp-exp, duration)
            exp = new_exp
        
        return res