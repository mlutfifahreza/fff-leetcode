class Solution:
    def rotatedDigits(self, n: int) -> int:
        # valid states
        # not 0 in the end
        # contains only flippable nums [0,1,8,2,5,6,9]
        nums_mapping = {
            0 : 0,
            1 : 1,
            8 : 8,
            2 : 5,
            5 : 2,
            6 : 9,
            9 : 6,
        }
        def is_valid(n):
            og_chars = []
            new_chars = []
            while n > 0:
                c = n % 10
                if c not in nums_mapping:
                    return False
                og_chars = [c] + og_chars
                new_chars = [nums_mapping[c]] + new_chars
                n //= 10
            # print(f'{og_chars} != {new_chars} = {og_chars != new_chars}')
            return og_chars != new_chars
        
        res = 0
        for i in range(1, n+1):
            res += is_valid(i)
            # print(f'processing i = {i} , res = {res}')
        return res