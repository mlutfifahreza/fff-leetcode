class Solution:
    def minOperations(self, s: str) -> int:
        mismatch0 = 0  # pattern starting with '0'
        mismatch1 = 0  # pattern starting with '1'
        
        for i, c in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'
            
            if c != expected0:
                mismatch0 += 1
            if c != expected1:
                mismatch1 += 1
        
        return min(mismatch0, mismatch1)