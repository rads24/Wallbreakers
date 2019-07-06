from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        patternDict = defaultdict(lambda: "")
        
        strList = str.split(" ")
        patternStr = ""
        
        if len(pattern) != len(strList):
            return False
        
        for i, char in enumerate(pattern):
            if char not in patternDict.keys() and strList[i] not in patternDict.values():
                patternDict[char] = strList[i]
         
        for char in pattern:
            patternStr += patternDict[char] + " "
    
        return str == patternStr.strip()