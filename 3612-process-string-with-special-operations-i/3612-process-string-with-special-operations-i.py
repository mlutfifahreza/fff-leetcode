class Solution:
    def processStr(self, s: str) -> str:
        res = ""

        for c in s:
            if c == '*':
                if len(res) > 0:
                    res = res[:-1]
            elif c == '#':
                res = res + res
            elif c == '%':
                new_res = ""
                i = 0
                max_i = len(res) - 1
                while i <= max_i:
                    new_res += res[max_i - i]
                    i += 1
                res = new_res
            else:
                res += c
            # print(c, res)
        
        return res