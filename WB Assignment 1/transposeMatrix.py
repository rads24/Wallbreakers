class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        
       # transposeA = [[0] * cols] * rows (this is wrong because multiplying by rows is just creating copies of the first row, which is why they are all just taking the same value)
    
        transposeA = [[0] * rows for i in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposeA[j][i] = A[i][j]

        return transposeA