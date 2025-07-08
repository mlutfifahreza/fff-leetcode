class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        # result = []
        
        # for i,w in enumerate(words):
        #     found = False
        #     for c in w:
        #         if found:
        #             continue
        #         if c == x:
        #             result.append(i)
        #             found = True
        
        # return result

        return [i for i, word in enumerate(words) if x in word]
