class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        total_substrings = n - k + 1
        total_possible = 2 ** k
        
        if total_substrings < total_possible:
            return False
        
        seen = set()
        
        for i in range(total_substrings):
            seen.add(s[i:i+k])
        
        return len(seen) == total_possible