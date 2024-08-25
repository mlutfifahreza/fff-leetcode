class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # a -> 0, b -> 1, ..., z -> 25
        def index(c):
            return ord(c) - ord('a')
        
        counter_p = [0]*26
        for c in p:
            counter_p[index(c)] += 1
        
        res = []

        # s = "abcde"
        # p = "bc"

        counter = [0]*26
        for i,c in enumerate(s):
            # invalidate
            if i >= len(p):
                counter[index(s[i-len(p)])] -= 1
            
            # count 
            counter[index(c)] += 1
            
            # validation
            # valid = True
            # for j in range(26):
            #     if counter[j] != counter_p[j]:
            #         valid = False
            #         break
            # if valid:
            #     res.append(i-len(p)+1)
            if counter == counter_p:
                res.append(i-len(p)+1)
        
        return res