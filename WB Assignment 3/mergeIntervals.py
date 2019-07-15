# This solution works for some but times out for others
# [[1,4],[5,6]] is timing out not sure why

"""
class Solution:
    def mergeSort(self, arr):
        if (len(arr) > 1): 
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            
            self.mergeSort(L)
            self.mergeSort(R)
            
            i = j = k = 0
            
            while i < len(L) and j < len(R):
                if L[i][0] < R[j][0]:
                    arr[k] = L[i]
                    i += 1
                elif L[i][0] == R[j][0]:
                    if L[i][1] < R[j][1]:
                        arr[k] = L[j]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                
                    
    def shouldMerge(self,listA, listB):
        if listA[1] >= listB[0]:
            return [listA[0], listB[1]]
        else:
            return listB
        
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        self.mergeSort(intervals)
        
        res = []
            
        if intervals[0][1] >= intervals[1][0]:
            res.append([intervals[0][0], intervals[1][1]])
            intervals.pop(0)
            intervals.pop(0)
        else:
            res = intervals
        
        while intervals:
            temp = self.shouldMerge(res[-1], intervals.pop(0))
            res.append(temp)
            
        return res
"""

class Solution:
             
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        
        res = []
        for pair in intervals:
            if not res or res[-1][1] < pair[0]:
                res.append(pair)
            else:
                res[-1][1] = max(res[-1][1], pair[1])
        return res
        