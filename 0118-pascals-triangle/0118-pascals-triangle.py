class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = []
            j = 0
            while j <= i:
                prev_row = i-1
                a, b = j-1, j
                # print(f"prev_row={prev_row}, a={a}, b={b}")
                if prev_row<0 or a<0 or b > i-1:
                    row.append(1)
                else:
                    row.append(rows[prev_row][a] + rows[prev_row][b])
                j += 1
            rows.append(row)
        return rows