class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        # O(n) 
        for y in range(len(strs[0])): # for reach string char
            for x in range(len(strs) - 1): # for each string , string n vs n+1
                if strs[x][y] > strs[x+1][y]:
                    res += 1
                    break
        
        return res