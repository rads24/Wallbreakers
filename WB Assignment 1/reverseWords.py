class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split(" ")
        for index, word in enumerate(strList):
            strList[index] = word[::-1]
        return ' '.join(strList)