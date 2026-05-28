class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = {}

        for i,n in enumerate(nums):
            if n not in d :
                d[n] = []
            d[n].append(i)
        INF = float('inf')
        res = INF
        for e in d.values():
            for i in range(len(e)-2):
                distance = (e[i+2] - e[i]) * 2
                res = min(res, distance)

        if res == INF:
            return -1
        
        return res