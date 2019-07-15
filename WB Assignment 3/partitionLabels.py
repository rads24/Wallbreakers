class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndex = {}
        for i, char in enumerate(S):
            lastIndex[char] = i
        
        res = []
        left = right = 0
        for i, char in enumerate(S):
            right = max(right, lastIndex[char])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res