class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        
        dic_sort = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        print(f"dic_sort={dic_sort}")

        res = [0]*k
        for i in range(k):
            res[i] = dic_sort[i][0]

        print(f"res={res}")
        return res