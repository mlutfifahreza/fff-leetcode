class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        once = set()
        multiple = set()

        for n in nums:
            if n in multiple:
                pass
            elif n in once:
                once.discard(n)
                multiple.add(n)
            else:
                once.add(n)
        
        return once.pop()