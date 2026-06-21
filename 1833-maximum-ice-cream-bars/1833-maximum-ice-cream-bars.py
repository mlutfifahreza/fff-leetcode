class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        res = 0
        i = 0
        n = len(costs)
        while coins > 0 and i < n:
            if costs[i] <= coins:
                res += 1
                coins -= costs[i]
            i += 1
        
        return res