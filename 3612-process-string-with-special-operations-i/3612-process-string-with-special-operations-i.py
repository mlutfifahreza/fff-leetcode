class Solution:
    """
    Processes a string based on special operational characters:
    '*' : Deletes the last character (Backspace).
    '#' : Duplicates the entire current string.
    '%' : Reverses the entire current string.
    """

    def processStr(self, s: str) -> str:
        # Using a list as a mutable stack to avoid O(N^2) string copy overhead
        res_stack: list[str] = []

        for char in s:
            if char == '*':
                if res_stack:
                    res_stack.pop()
            
            elif char == '#':
                # O(K) complexity where K is current length. 
                # Note: Watch out for memory limits if '#' appears sequentially.
                res_stack.extend(res_stack)
            
            elif char == '%':
                # In-place reversal of the list is highly optimized in C (O(K))
                res_stack.reverse()
            
            else:
                res_stack.append(char)
        
        # Single O(N) join operation at the end
        return "".join(res_stack)