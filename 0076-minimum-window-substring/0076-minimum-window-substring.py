class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Length of the strings
        m, n = len(s), len(t)

        if n > m:
            return ""  # If t is longer than s, it's impossible to have a window.

        INDEX_MAX = 128  # Expanded to accommodate the entire ASCII range

        # Function to get the index of a character
        def index(c):
            return ord(c)

        # Frequency array for characters in t
        char_t = [0] * INDEX_MAX
        for c in t:
            char_t[index(c)] += 1

        # Helper function to check if the current window contains all characters in t
        def is_valid(sub_list, t_list):
            for i in range(INDEX_MAX):
                if sub_list[i] < t_list[i]:
                    return False
            return True

        # Sliding window pointers and the tracker for window characters
        left = 0
        min_length = float('inf')
        start = 0
        tracker = [0] * INDEX_MAX

        for right in range(m):
            tracker[index(s[right])] += 1

            # Try to contract the window until it's no longer valid
            while is_valid(tracker, char_t):
                if right - left < min_length:
                    min_length = right - left
                    start = left
                
                tracker[index(s[left])] -= 1
                left += 1

        # If no valid window was found, return an empty string
        if min_length == float('inf'):
            return ""
        
        # Return the minimum window
        return s[start:start + min_length + 1]
