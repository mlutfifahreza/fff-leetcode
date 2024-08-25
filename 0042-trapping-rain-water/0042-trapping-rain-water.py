class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        l, r = 0, len(h)-1

        max_left, max_right = h[l], h[r]
        res = 0
        while l < r:
            # process left
            if max_left <= max_right:
                l += 1
                res += max(0, max_left - h[l])
                max_left = max(max_left, h[l])
            # process right
            else:
                r -= 1
                res += max(0, max_right - h[r])
                max_right = max(max_right, h[r])
        
        return res