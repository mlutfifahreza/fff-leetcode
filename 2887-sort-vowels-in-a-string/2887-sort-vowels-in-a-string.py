class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowels_index = []
        vowels_const = (
            'A', 'a', 
            'E', 'e', 
            'I', 'i', 
            'O', 'o', 
            'U', 'u', 
            )
        for i in range(len(s)):
            c = s[i]
            if c in vowels_const:
                vowels.append(c)
                vowels_index.append(i)
        
        if len(vowels) == 0:
            return s
        
        vowels = sorted(vowels)
        t = [c for c in s]
        # print(f"s={s}, t={t}, vowels_index={vowels_index}")
        for i in range(len(vowels_index)):
            t[vowels_index[i]] = vowels[i]
        
        return "".join(t)