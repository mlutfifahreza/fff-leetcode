class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths aren't equal, s can never be rotated into goal
        if len(s) != len(goal):
            return False
        
        # Check if goal exists within the concatenated string
        return goal in (s + s)