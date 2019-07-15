class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        min = 0
        max = len(A) - 1
        
        if (len(A) < 3): return -1
        
        while min <= max:
            avg = (min + max) // 2
            if A[avg - 1] < A[avg] and A[avg + 1] < A[avg]:
                return avg
            else:
                if A[avg + 1] > A[avg]:
                    min = avg + 1
                else:
                    max = avg - 1
        return -1

"""
## With recursion
class Solution(object):
    def binSearch(self, A, start, end):
        mid = start + (end - start) / 2
        
        if A[mid] > A[mid - 1] and A[mid] > A[mid+1]:
            return mid
        elif A[mid] < A[mid - 1]:
            return self.binSearch(A, start, mid-1)
        else:
            return self.binSearch(A, mid+1, end)
        return -1
        
    def peakIndexInMountainArray(self, A):
        
        if len(A) < 3:
            return -1
        return self.binSearch(A, 0, len(A)-1)

"""