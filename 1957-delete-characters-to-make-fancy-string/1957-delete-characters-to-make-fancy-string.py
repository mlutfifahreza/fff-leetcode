class Solution:
    def makeFancyString(self, s: str) -> str:
        counter = 0
        last_c = ''

        res = ''

        for c in s:
            if c == last_c:
                if counter == 2:
                    continue
                else:
                    res += c
                    counter += 1
            else:
                last_c = c
                res += c
                counter = 1
        
        return res