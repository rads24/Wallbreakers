import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numsCounter = collections.Counter(nums)
        twice = -1
        zero = -1
        
        
        for i in range (1, len(nums)+1):
            if numsCounter[i] == 2:
                twice = i
            elif i not in numsCounter.keys():
                zero = i
        
        return [twice, zero]
        