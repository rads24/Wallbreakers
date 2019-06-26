class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        # create 2 arrays and append values based on even and odd and then combine the two arrays
        
        evenList = []
        oddList = []
        
        for val in A:
            if val % 2 == 0:
                evenList.append(val)
            else:
                oddList.append(val)
                
        return evenList + oddList