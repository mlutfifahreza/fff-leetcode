class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k % total

        # print(f"total = {total} k = {k}")

        for i,v in enumerate(chalk):
            # print(f"i = {i} v = {v}")
            if v > k:
                return i
            k -= v
        
        return 0