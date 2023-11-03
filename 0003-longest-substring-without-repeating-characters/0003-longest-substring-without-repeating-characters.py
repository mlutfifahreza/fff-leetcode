class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hold_s = deque()
        max_len = 0
        max_index = len(s)-1

        for i in range(len(s)):
            c = s[i]
            
            if c not in hold_s:
                hold_s.append(c)
            else:
                n = len(hold_s)
                if n > max_len: max_len = n

                while hold_s.popleft() != c:
                    pass
                hold_s.append(c)
            
            if i == max_index:
                n = len(hold_s)
                if n > max_len: max_len = n
        
        return max_len 