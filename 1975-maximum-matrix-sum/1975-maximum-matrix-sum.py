class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cur_sum = 0
        cur_min = float('inf')
        negative_count = 0

        for row in matrix:
            for n in row:
                pos_n = abs(n)
                cur_sum += pos_n
                cur_min = min(cur_min, pos_n)
                if n < 0: negative_count += 1

        # print("cur_sum", cur_sum)
        # print("cur_min", cur_min)
        # print("negative_count", negative_count)
        
        if negative_count % 2 == 1:
            return cur_sum - 2*cur_min
        else:
            return cur_sum