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
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
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
                
                
    def arrayPairSum(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total



"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total
"""