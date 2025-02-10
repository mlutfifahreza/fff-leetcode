class Solution:
    def clearDigits(self, s: str) -> str:
        result = []

        for c in s:
            # print(f'c={c}')
            if c in "0123456789":
                # print("popping")
                if result: result.pop()
                # print(f'result={result}')
            else:
                result.append(c)
        
        # print(f'result={result}')
        return ''.join(result)