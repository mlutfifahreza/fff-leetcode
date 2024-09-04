class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(cur_li, rest):
            # print(f"cur_li={cur_li} rest={rest}")
            if len(rest) == 0:
                res.append(cur_li)
                return
            
            for i, v in enumerate(rest):
                new_li = cur_li + [v]
                recur(new_li, rest[:i] + rest[i+1:])
            
        recur([], nums)

        return res