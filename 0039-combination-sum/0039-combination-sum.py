class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recur(curli, curval, rest):
            if curval < 0:
                return
            elif curval == 0:
                res.append(curli)
            else:
                for i, n in enumerate(rest):
                    recur(curli+[n], curval-n, rest[i:])
        
        recur([], target, candidates)

        return res