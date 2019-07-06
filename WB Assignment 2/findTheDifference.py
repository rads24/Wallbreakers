import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sDict = collections.Counter(s)
        tDict = collections.Counter(t)
        
        
        uniqueValDict = tDict - sDict
        
        uniqueVal = ""
        for key in uniqueValDict:
            uniqueVal += key
            
        return uniqueVal