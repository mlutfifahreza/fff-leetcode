class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for ch in s:
        #     # print(stack)
        #     try:
        #         if ch == ")":
        #             if stack[-1] == "(": stack.pop()
        #             else: return False
        #         elif ch == "}":
        #             if stack[-1] == "{": stack.pop()
        #             else: return False
        #         elif ch == "]":
        #             if stack[-1] == "[": stack.pop()
        #             else: return False
        #         else:
        #             stack.append(ch)
        #     except:
        #         return False
        # if len(stack) > 0:
        #     return False
        # return True
        right = ("}", "]", ")")

        dq = deque()
        for ch in s:
            if ch in right:
                if len(dq) == 0:
                    return False
                left = dq.pop()
                if left == "(" and ch is not ")":
                    return False
                elif left == "{" and ch is not "}":
                    return False
                elif left == "[" and ch is not "]":
                    return False
            else:
                dq.append(ch)
        return len(dq) == 0