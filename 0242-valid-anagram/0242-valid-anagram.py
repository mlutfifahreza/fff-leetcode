class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ar1 = [0] * 26
        ar2 = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')
            ar1[idx] += 1
        
        for c in t:
            idx = ord(c) - ord('a')
            ar2[idx] += 1
        
        for a,b in zip(ar1, ar2):
            if a != b:
                return False
        
        return True