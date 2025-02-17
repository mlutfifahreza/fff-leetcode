class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        final_set = set()
        
        def recur(c, cur, rest):
            # print()
            # print(f'recur({c}, {cur}, {rest})')
            word = cur + c
            final_set.add(word)
            # print(f"word = {word} final_set = {final_set}")

            # if not rest : return

            for i,v in enumerate(rest):
                recur(rest[i], word, rest[0:i] + rest[i+1:len(rest)])
        
        recur("", "", tiles)

        return len(final_set) - 1