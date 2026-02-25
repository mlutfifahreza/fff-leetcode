class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def bitc(n):
            res = 0
            while n > 0:
                res += n & 1
                n >>= 1
            return res
        
        dic = {}
        for n in arr:
            k = bitc(n)
            if k not in dic:
                dic[k] = []
            dic[k].append(n)
        
        sorted_key = sorted(dic.keys())
        res = []
        for k in sorted_key:
            val = dic[k]
            res.extend(sorted(val))

        return res