class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # holds [index, temp]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append([i, temp])
        
        return res