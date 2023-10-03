class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result_hold = []
        for i in range(len(mat[0]) + 1):
            result_hold.append([])
        # print(result_hold)
        for i in range(len(mat)):
            row = mat[i]
            assigned = False
            for j in range(len(row)):
                if row[j] == 0:
                    result_hold[j].append(i)
                    assigned = True
                    break
            if not assigned:
                result_hold[len(row)].append(i)
            # print(result_hold)
        counter = 0
        result = []
        for row in result_hold:
            for r in row:
                result.append(r)
                counter += 1
                if counter == k:
                    return result