import collections
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = len(g)
        cookies = len(s)
        
        g.sort()
        s.sort()
        sizeDict = collections.Counter(s)
        keyCount = 0
        keys = list(sizeDict.keys())
        
        happyChildren = 0
        
        for greed in g:
            while keys and greed > keys[0]:
                keys.pop(0)
            if keys and greed <= keys[0] and sizeDict[keys[0]] != 0:
                sizeDict[keys[0]] -= 1
                if sizeDict[keys[0]] == 0: 
                    sizeDict.pop(keys[0])
                    keys.pop(0)
                happyChildren += 1 