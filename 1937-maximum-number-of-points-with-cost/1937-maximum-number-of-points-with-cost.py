class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return max(points[0])

        w = len(points[0])
        
        prev_max_left = points[0]
        prev_max_right = points[0]

        for p_list in points[1:]:
            # search from left
            print("prev_max_left", prev_max_left)
            print("prev_max_right", prev_max_right)
            prev_max_new_left = [0] * w
            max_left_prev_i = 0
            for i in range(w):
                val_i = p_list[i] + prev_max_left[i]
                val_i_left = p_list[i] + prev_max_left[max_left_prev_i] - abs(i - max_left_prev_i)
                if val_i > val_i_left:
                    max_left_prev_i = i
                    prev_max_new_left[i] = val_i
                else:
                    prev_max_new_left[i] = val_i_left
            print("prev_max_new_left", prev_max_new_left)
            prev_max_left = prev_max_new_left

            # search from right
            prev_max_new_right = [0] * w
            max_right_prev_i = w-1
            for i in range(w-1, -1, -1):
                val_i = p_list[i] + prev_max_right[i]
                val_i_right = p_list[i] + prev_max_right[max_right_prev_i] - abs(i - max_right_prev_i)
                if val_i > val_i_right:
                    max_right_prev_i = i
                    prev_max_new_right[i] = val_i
                else:
                    prev_max_new_right[i] = val_i_right

            print("prev_max_new_right", prev_max_new_right)
            prev_max_right = prev_max_new_right

            print()
        
        return max(max(prev_max_left), max(prev_max_right))