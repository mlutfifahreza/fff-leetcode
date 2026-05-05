from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = 0
        countO = 0
        
        # 1. Count the pieces
        for row in board:
            for char in row:
                if char == 'X': countX += 1
                elif char == 'O': countO += 1
        
        # Rule: X always starts first, so X count == O count or O count + 1
        if not (countX == countO or countX == countO + 1):
            return False
        
        # 2. Helper to check if a specific player has won
        def check_win(p):
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == p for j in range(3)): return True
                if all(board[j][i] == p for j in range(3)): return True
            # Check diagonals
            if board[0][0] == board[1][1] == board[2][2] == p: return True
            if board[0][2] == board[1][1] == board[2][0] == p: return True
            return False

        x_wins = check_win('X')
        o_wins = check_win('O')

        # 3. Final Validation Logic
        # Both cannot win at the same time
        if x_wins and o_wins:
            return False
        
        # If X wins, X must have exactly one more piece than O
        if x_wins and countX != countO + 1:
            return False
        
        # If O wins, counts must be equal (since O moves second)
        if o_wins and countX != countO:
            return False
            
        return True