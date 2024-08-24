class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        exp = -1

        for t in timeSeries:
            res += duration if t > exp else t + duration - 1 - exp
            exp = t + duration - 1
        
        return res
