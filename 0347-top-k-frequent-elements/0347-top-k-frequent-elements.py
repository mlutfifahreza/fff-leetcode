class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the elements, put in maps {el -> count} O(n)
        ct = {}
        for n in nums:
            if n not in ct:
                ct[n] = 0
            ct[n] += 1
        # print(f'ct = {ct}')
        
        # put to array [count] -> (list of element) O(n)
        arr = [list() for i in range(len(nums)+1)]
        for el, ct in ct.items():
            arr[ct].append(el)
        # print(f'arr = {arr}')

        # from last index -> start , return k elements
        i = len(nums)
        res = []
        while len(res) < k and i > 0:
            res.extend(arr[i])
            i -= 1
        # print(f'res = {res}')
        
        return res