class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx-sx)
        dy = abs(fy-sy)
        if dx == 0 and dy == 0:
            return t != 1

        diagonal = min(dx,dy)
        straight = max(dx,dy) - min(dx,dy)
        print(f"diagonal + straight={diagonal + straight} < t {t}")
        return t >= (diagonal + straight) 