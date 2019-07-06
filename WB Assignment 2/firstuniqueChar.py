import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = collections.Counter(s)
        
        for char in s:
            if charCount[char] == 1:
                return s.index(char)
            
        return -1