class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowels_index = []

        vowels_set = set("AEIOUaeiou")

        # collect vowels and their indices
        for i, ch in enumerate(s):
            if ch in vowels_set:
                vowels.append(ch)
                vowels_index.append(i)

        # if no vowels, return original string
        if not vowels:
            return s

        # sort vowels
        vowels.sort()

        # build new string
        s_list = list(s)
        for i, idx in enumerate(vowels_index):
            s_list[idx] = vowels[i]

        return "".join(s_list)
