class Solution:
    def sum_digit(self, n):
        res = 0
        while n > 0:
            res += n%10
            n //= 10
        return int(res)

    def maximumSum(self, nums: List[int]) -> int:
        memo = {} # sum_digit -> max_num
        result = -1
        for n in nums:
            # print("n = ", n)
            sum_digit = self.sum_digit(n)
            max_before = memo.get(sum_digit, None)
            if max_before:
                result = max(result, max_before + n)
                if n > max_before:
                    memo[sum_digit] = n
            else:
                memo[sum_digit] = n
            # print(f'sum_digit = {sum_digit} max_before = {max_before} memo = {memo} ')
        
        return result