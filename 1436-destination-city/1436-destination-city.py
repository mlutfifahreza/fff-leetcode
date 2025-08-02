class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cm = {}

        for a,b in paths:
            cm[a] = b
        
        result = paths[0][0]

        while result in cm:
            result = cm[result]
        
        return result