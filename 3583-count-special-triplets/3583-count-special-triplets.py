class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counter_left = dict()
        counter_right = dict()
        for n in nums:
            if n not in counter_right:
                counter_left[n] = 0
                counter_right[n] = 0
            counter_right[n] += 1
        
        # print(f'counter_left = {counter_left}')
        # print(f'counter_right = {counter_right}')

        def get_valid_comb(n):
            if n not in counter_left:
                return 0
            if n not in counter_right:
                return 0
            return counter_left[n] * counter_right[n]

        res = 0
        for n in nums:
            counter_right[n] -= 1
            res += get_valid_comb(n * 2)
            counter_left[n] += 1
            # print(f'n = {n}')
            # print(f'res = {res}')
            # print(f'counter_left = {counter_left}')
            # print(f'counter_right = {counter_right}')

        return res % (pow(10,9) + 7)