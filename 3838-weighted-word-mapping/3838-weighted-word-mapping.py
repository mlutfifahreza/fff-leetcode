class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            word_sum = 0
            for char in word:
                idx = ord(char) - ord('a')
                word_sum += weights[idx]
                
            res += chr(ord('z') - word_sum%26)
        
        return res