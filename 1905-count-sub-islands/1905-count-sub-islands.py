class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.m, self.n = len(grid1), len(grid1[0])
        self.grid1 = grid1
        self.grid2 = grid2
        q = []
        self.visited = []
        for _ in range(self.m):
            self.visited.append([False] * self.n)

        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid2[i][j] == 1 and not self.visited[i][j]:
                    if self.is_island_valid(i,j):
                        res += 1
        
        # [print(v) for v in self.visited]
        
        return res
    
    def is_island_valid(self, i, j):
        if not (0 <= i < self.m):
            return True
        if not (0 <= j < self.n):
            return True

        if self.visited[i][j]:
            return True
        
        if self.grid2[i][j] == 0:
            return True
        
        if self.grid1[i][j] == 0:
            return False
        else:
            self.visited[i][j] = True
            top, right = self.is_island_valid(i-1,j), self.is_island_valid(i,j+1)
            down, left = self.is_island_valid(i+1,j), self.is_island_valid(i,j-1)
            return top and right and down and left