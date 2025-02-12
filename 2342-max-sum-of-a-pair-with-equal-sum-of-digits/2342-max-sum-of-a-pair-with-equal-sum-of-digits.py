class Solution:
    def sum_digit(self, n):
        res = 0
        while n > 0:
            res += n%10
            n //= 10
        return int(res)

    def maximumSum(self, nums: List[int]) -> int:
        max_of_sum_digit = {} # sum_digit -> max_num
        result = -1
        for n in nums:
            # print("n = ", n)
            sum_digit = self.sum_digit(n)
            max_before = max_of_sum_digit.get(sum_digit, None)
            if max_before:
                result = max(result, max_before + n)
                if n > max_before:
                    max_of_sum_digit[sum_digit] = n
            else:
                max_of_sum_digit[sum_digit] = n
            # print(f'sum_digit = {sum_digit} max_before = {max_before} max_of_sum_digit = {max_of_sum_digit} ')
        
        return result