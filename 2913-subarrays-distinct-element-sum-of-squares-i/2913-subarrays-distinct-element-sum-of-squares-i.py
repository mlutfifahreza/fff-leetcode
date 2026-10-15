class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i, n):
                counter = {}
                for x in range(i,j+1):
                    num = nums[x]
                    if num not in counter:
                        counter[num] = 1
                this_count = pow(len(counter), 2)
                res += this_count
                # print(f'processing i j {i} {j} | counter {counter} this_count {this_count} res {res} ')

        return res