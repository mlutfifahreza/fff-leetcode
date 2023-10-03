class Solution:
    def sortString(self, s: str) -> str:
        char_count = [0] * 26
        for c in s:
            idx = ord(c) % 97
            char_count[idx] += 1
        
        result = ""
        direction = 1  # 1 right, -1 left
        while 1:
            sum = 0
            first, last = (0, 26) if (direction == 1) else (25, -1)
            for i in range(first, last, direction):
                if char_count[i] > 0:
                    char_count[i] -= 1
                    result += chr(97 + i)
                    sum += 1
            # switch direction
            direction *= -1
            # all has assigned
            if sum == 0:
                return result