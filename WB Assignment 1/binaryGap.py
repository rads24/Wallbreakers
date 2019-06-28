class Solution:
    def binaryGap(self, N: int) -> int:
        binString = bin(N)[2:]
        left = right = 0
        gap = 0
        while left < len(binString):
            if binString[left] == 1:
                for j in range(left + 1, len(s)):
                    if s[j] == 1:
                        right = j
                        break
                curgap = right - left
                if curgap > gap:
                    gap = curgap
                left = right
            else:
                left += 1
        return gap
    
    #struggling to debug this