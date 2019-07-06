import collections
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        l = r = 0
        pCount = collections.Counter(p)
        window = dict()
        required = len(pCount)
        formed = 0
        length = len(p)
        
        indexArray = []
        
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            
            if (s[r] in pCount and window[s[r]] == pCount[s[r]]):
                formed += 1
                
            while l <= r and formed == required:
                if r - l + 1 == length:
                    indexArray.append(l)
                   
                window[s[l]] -= 1
                
                if s[l] in pCount and window[s[l]] < pCount[s[l]]:
                    formed -= 1
                    
                l += 1
            r += 1
        return indexArray