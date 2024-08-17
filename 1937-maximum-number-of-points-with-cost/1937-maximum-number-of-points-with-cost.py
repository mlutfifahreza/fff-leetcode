class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return max(points[0])

        w = len(points[0])
        prev_max = [x for x in points[0]]
        for p_list in points[1:]:
            # search from left
            prev_max_left = [0] * w
            max_left = 0
            for i in range(w):
                prev_max_left[i] = max_left = max(max_left-1, prev_max[i])
            # print("prev_max_left", prev_max_left)

            # search from right
            prev_max_right = [0] * w
            max_right = 0
            for i in range(w-1, -1, -1):
                prev_max_right[i] = max_right = max(max_right-1, prev_max[i])
            # print("prev_max_right", prev_max_right)

            for i in range(w):
                prev_max[i] = max(prev_max_left[i], prev_max_right[i]) + p_list[i]
            # print("prev_max", prev_max)
            # print()
        
        return max(prev_max)