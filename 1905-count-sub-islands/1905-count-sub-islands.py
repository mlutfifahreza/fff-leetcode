class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.m, self.n = len(grid1), len(grid1[0])
        self.grid1 = grid1
        self.grid2 = grid2

        def is_island_valid(i, j):
            if not (0 <= i < self.m and 0 <= j < self.n) or grid2[i][j] == 0:
                return True
            if grid1[i][j] == 0:
                return False
            
            # Mark as visited
            grid2[i][j] = 0
            
            # Recursively check all neighbors
            valid = True
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not is_island_valid(x, y):
                    valid = False
            
            return valid

        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid2[i][j] == 1 and is_island_valid(i, j):
                    res += 1

        return res
