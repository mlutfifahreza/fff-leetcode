class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(b[j]) - ord('0')
                j -= 1

            res.append(str(carry & 1))
            carry >>= 1

        return ''.join(reversed(res))
