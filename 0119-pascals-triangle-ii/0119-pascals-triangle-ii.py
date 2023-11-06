class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        i = 2
        result = [1,1]
        while i <= rowIndex:
            j = 0
            new_result = [1]
            while j < len(result)-1:
                new_result.append(result[j] + result[j+1])
                j += 1
            new_result.append(1)
            result = new_result
            i += 1
        return result