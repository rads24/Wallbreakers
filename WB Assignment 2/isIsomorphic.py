from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        sDict = defaultdict(lambda: "")
        
        for i, char in enumerate(s):
            if char not in sDict.keys() and t[i] not in sDict.values():
                sDict[char] = t[i]
        
        myT = ""
        for char in s:
            myT += sDict[char]
            
        return t == myT