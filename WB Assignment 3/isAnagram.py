
class Solution:
    def mergeSort(self, arr):
        if (len(arr)) > 1:
            mid = len(arr) // 2
            L = (arr[:mid])
            R = (arr[mid:])
            
            self.mergeSort(L)
            self.mergeSort(R)
            
            i = j = k = 0
            
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                
            while i < len(L):
                arr[k] = L[i]
                k += 1
                i += 1
                
            while j < len(R):
                arr[k] = R[j]
                k += 1
                j += 1
        
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        s = list(s)
        t = list(t)
        self.mergeSort(s)
        self.mergeSort(t)
        return s == t
    
    # with sorting


"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
"""