class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(left, right, s):
            if left + right == 2*n:
                print(f"adding '{s}'")
                res.append(s)
            else:
                if left < n:
                    dfs(left+1, right, s+'(')
                
                if right < left:
                    dfs(left, right+1, s+')')
        
        res = []
        dfs(0,0,'')

        return res