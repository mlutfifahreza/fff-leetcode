class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_z = False

        for c in s:
            if found_z and c == '1':
                return False
            elif c == '0':
                found_z = True

        return True