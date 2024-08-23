class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # row: flip if index 0 is 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = (grid[i][j] + 1) % 2
        
        # [print(g) for g in grid]

        for j in range(n):
            one,zero = 0,0
            for i in range(m):
                if grid[i][j] == 0:
                    zero += 1
                else:
                    one += 1
            if zero > one:
                for i in range(m):
                    grid[i][j] = (grid[i][j] + 1) % 2
                # print()
                # [print(g) for g in grid]
        
        def to_int(bin_list):
            p = len(bin_list)
            res = 0
            for i in range(p):
                if bin_list[i] == 1:
                    res += pow(2, p-i-1)
            # print(bin_list, res)
            return res

        return sum([to_int(g) for g in grid])