class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # print("row, col", row, col)
        if row < 3 or col < 3:
            return 0

        result = 0
        for curr_r in range(row-2):
            for curr_c in range(col-2):
                a,b,c = grid[curr_r][curr_c], grid[curr_r][curr_c+1], grid[curr_r][curr_c+2]
                d,e,f = grid[curr_r+1][curr_c], grid[curr_r+1][curr_c+1], grid[curr_r+1][curr_c+2]
                g,h,i = grid[curr_r+2][curr_c], grid[curr_r+2][curr_c+1], grid[curr_r+2][curr_c+2]

                # print(f"{a},{b},{c}")
                # print(f"{d},{e},{f}")
                # print(f"{g},{h},{i}")
                # print()

                nums = set([a,b,c, d,e,f, g,h,i])
                if len(nums) != 9 or min(nums) < 1 or max(nums) > 9:
                    continue

                if a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g:
                    result += 1
        
        return result