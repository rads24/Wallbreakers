class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        total = 0
        difference = x ^ y
        
        while difference > 0:
            if (difference & 1 == 1):
                total += 1
            difference = difference >> 1
        return total