from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # cannot figure out how to solve it without extra space
        
        numDict = defaultdict(int)
        for val in nums:
            numDict[val] += 1
        
        for key in numDict:
            if numDict[key] == 1: return key
            else: continue