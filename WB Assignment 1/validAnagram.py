class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        sSet = set(s)
        tSet = set(t)
        
        if sSet != tSet: return False    #all characters are not same
        
        #now check count of characters
        
        for char in s:
            if char in sDict:
                continue
            else:
                sDict[char] = s.count(char)
        for char in t:
            if char in tDict:
                continue
            else:
                tDict[char] = t.count(char)
        for key in sDict:
            if sDict[key] != tDict[key]:
                return False
        return True