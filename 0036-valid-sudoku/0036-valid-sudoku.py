class Solution:
    def checkValid(self, li):
        nums = set()
        for e in li:
            if '0' <= e <= '9':
                if e in nums:
                    return False
                else:
                    nums.add(e)
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        for i in range(9):
            if not self.checkValid(board[i]):
                return False
        # check vertical
        for j in range(9):
            li = []
            for i in range(9):
                li.append(board[i][j])
            if not self.checkValid(li):
                return False
        # check 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                li = []
                for k in range(3):
                    for l in range(3):
                        li.append(board[i+k][j+l])
                if not self.checkValid(li):
                    return False
        return True