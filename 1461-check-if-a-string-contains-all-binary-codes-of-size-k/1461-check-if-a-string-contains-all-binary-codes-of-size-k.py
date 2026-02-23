class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        check = {}
        n = len(s)

        for i in range(n-k+1):
            substr = s[i:i+k]
            # print(f'substr = {substr}')
            check[substr] = True
        # print(f'check = {check}')

        exp = pow(2,k)
        # print(f'exp= {exp}')

        return exp == len(check)