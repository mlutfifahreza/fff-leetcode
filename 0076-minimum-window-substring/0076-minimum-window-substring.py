class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)

        INDEX_MAX = 60

        def index(c):
            return ord(c) - ord("A")

        char_t = [0]*INDEX_MAX
        for c in t:
            char_t[index(c)] += 1

        def is_valid(sub_list, t_list):
            for i in range(INDEX_MAX):
                if sub_list[i] < t_list[i]:
                    return False
            return True

        # slide_window
        a,b = -99999, 999999
        l = 0
        tracker = [0]*INDEX_MAX
        for r in range(m):
            tracker[index(s[r])] += 1
            while is_valid(tracker, char_t):
                tracker[index(s[l])] -= 1
                if r-l < b-a:
                    a,b = l,r
                l += 1

        if a == -99999:
            return ""
        return s[a:b+1]