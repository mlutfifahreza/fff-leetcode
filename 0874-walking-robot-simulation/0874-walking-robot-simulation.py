class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [
            [0, 1], # north
            [1, 0], # east
            [0, -1], # south
            [-1, 0], # west
        ]

        x, y, d, res = 0, 0, 0, 0

        obstacles = set([f'{x}.{y}' for x,y in obstacles])

        for c in commands:
            # print(f"c={c}")
            if c == -2:
                d = (d-1) % 4
                # print(f"d={d} dir={directions[d]}")
            elif c == -1:
                d = (d+1) % 4
                # print(f"d={d} dir={directions[d]}")
            else:
                while c:
                    xn, yn =  x + directions[d][0] , y + directions[d][1]
                    if f'{xn}.{yn}' in obstacles:
                        c = 0
                    else:
                        c -= 1
                        x,y = xn, yn
                        res = max(res, x*x + y*y)
                        # print(f"x={x} y={y} c={c} res={res} ")
        
        return res