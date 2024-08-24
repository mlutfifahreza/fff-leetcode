class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {}
        self.target = target
        self.nums = nums
        self.len = len(nums)
        self.memo = {}
        return self.dfs(0, 0)
    
    def key(self, i, v):
        return f'{i},{v}'

    def dfs(self, i, v):
        key = self.key(i,v)
        if key in self.memo:
            return self.memo[key]

        if i == self.len:
            if v == self.target:
                return 1
            else:
                return 0
        
        pos = self.dfs(i+1, v + self.nums[i])
        neg = self.dfs(i+1, v - self.nums[i])

        res = pos + neg
        self.memo[key] = res
        return res