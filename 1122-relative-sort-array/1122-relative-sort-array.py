class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {}
        for v in arr2:
            counter[v] = 0
        
        rest = []
        for v in arr1:
            if v in counter:
                counter[v] += 1
            else:
                rest.append(v)
        
        result = []
        for v in arr2:
            for i in range(counter[v]):
                result.append(v)
        
        # print("counter", counter)
        # print("result", result)
        # print("rest", rest)
        
        return result + sorted(rest)