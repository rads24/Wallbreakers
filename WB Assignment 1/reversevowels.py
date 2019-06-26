class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vowelIndex = []
        for i, char in enumerate(s):
            if char in vowelSet: 
                vowelIndex.append(i)
        sCopy = ""
        if not vowelIndex:
            return s
        for char in s:
            if char not in vowelSet:
                sCopy += char
            else:
                sCopy += s[vowelIndex.pop()]
        return sCopy