class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        def str_to_list(s):
            res = [0]*26
            for c in s:
                res[ord(c) - 97] += 1
            # print(f"res={res}")
            return res

        def convert_list_to_key(li):
            return ".".join(map(str,li))
        
        groups = {}

        for s in strs:
            key = convert_list_to_key(str_to_list(s))
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        
        return list(groups.values())