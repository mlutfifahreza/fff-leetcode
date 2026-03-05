class Solution:
    def minOperations(self, s: str) -> int:
        a,b = 0,0

        check = '0'
        for c in s:
            if c == check:
                a += 1
            else:
                b += 1
            if check == '0':
                check = '1'
            else:
                check = '0'
            # print(f'check, a, b = {check}, {a}, {b}')
        
        return min(a,b)