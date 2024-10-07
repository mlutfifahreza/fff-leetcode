class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif c == "D" and stack[-1] == "C":
                stack.pop()
            elif c == "B" and stack[-1] == "A":
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack)