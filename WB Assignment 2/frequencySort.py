import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        letters = collections.Counter(s)
        
        mostCommon = letters.most_common()
        
        res = ""
        for char, count in mostCommon:
            res += (char * count)
        
        return res