class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def recur(cur, nums):
            # print(f"cur={cur} nums={nums}")
            if len(nums) == 0:
                return

            for i, n in enumerate(nums):
                cur_res = cur + [n]
                res.append(cur_res)
                recur(cur_res, nums[(i+1):])
        
        recur([], nums)

        return res