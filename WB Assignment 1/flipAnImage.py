class Solution:
    
    def invert (self, row):
        for i in range(len(row)):
            if row[i] == 1:
                row[i] = 0
            else:
                row[i] = 1
        return row
    
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(A):
            row = self.invert(row[::-1])
            A[i] = row
        return A