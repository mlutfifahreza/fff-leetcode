class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [
            (0, 1),   # north
            (1, 0),   # east
            (0, -1),  # south
            (-1, 0),  # west
        ]

        x, y, d, res = 0, 0, 0, 0

        obstacles_set = set(map(tuple, obstacles))

        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                for _ in range(c):
                    xn, yn = x + directions[d][0], y + directions[d][1]
                    if (xn, yn) in obstacles_set:
                        break
                    x, y = xn, yn
                    res = max(res, x * x + y * y)
        
        return res
