class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        
        def left(i):
            return (i-1) % len(words)

        def right(i):
            return (i+1) % len(words)

        def distance(i):
            d = abs(i - startIndex)
            dd = len(words) - d
            return min(d, dd)

        l,r = left(startIndex), right(startIndex)
        while l != r:
            if words[r] == target:
                # print(f'returning r abs({r}-{startIndex})')
                return distance(r)
            if words[l] == target:
                # print(f'returning l abs({l}-{startIndex})')
                return distance(l)
            l,r = left(l), right(r)
        
        if words[r] == target:
            # print(f'returning r abs({r}-{startIndex})')
            return distance(r)
        if words[l] == target:
            # print(f'returning l abs({l}-{startIndex})')
            return distance(l)
        
        return -1