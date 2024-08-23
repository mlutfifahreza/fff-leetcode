class Solution:
    def fractionAddition(self, expression: str) -> str:
        s = expression

        i = 0
        n = len(s)
        num, denum = 0, 1
        while i < n:
            # check sign
            negative = False
            if s[i] in "+-":
                if s[i] == "-":
                    negative = True
                i += 1

            # get num
            cur_num = 0
            while s[i] in "1234567890":
                # print(s[i], "->", int(s[i]))
                cur_num = cur_num * 10 + int(s[i])
                i += 1
            if negative:
                cur_num *= -1
            # print("cur_num", cur_num)

            # skip /
            i += 1

            # get denum
            cur_denum = 0
            while i<n and s[i] in "1234567890":
                # print(s[i], "->", int(s[i]))
                cur_denum = cur_denum * 10 + int(s[i])
                i += 1
            # print("cur_denum", cur_denum)

            # count
            num = num * cur_denum + cur_num * denum
            denum = denum * cur_denum
            # print("num, denum ", num, denum)
            # print()
        
        # simplify
        def get_gcd(a,b):
            if(b == 0):
                return abs(a)
            else:
                return get_gcd(b, a % b)
        
        gcd = get_gcd(num, denum)
        num //= gcd
        denum //= gcd

        # return
        return f"{num}/{denum}"