class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            # print(stack)
            try:
                if ch == ")":
                    if stack[-1] == "(": stack.pop()
                    else: return False
                elif ch == "}":
                    if stack[-1] == "{": stack.pop()
                    else: return False
                elif ch == "]":
                    if stack[-1] == "[": stack.pop()
                    else: return False
                else:
                    stack.append(ch)
            except:
                return False
        if len(stack) > 0:
            return False
        return True