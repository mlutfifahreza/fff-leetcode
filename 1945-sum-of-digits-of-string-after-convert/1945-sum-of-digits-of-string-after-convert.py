class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = ""
        for c in s:
            n += str(ord(c) - ord('a') + 1)
        # print(f"n={n}")
        
        n = int(n)
        for _ in range(k):
            temp = n
            n = 0
            while temp:
                n += temp % 10
                temp //= 10
            # print(f"n={n}")
        
        return n