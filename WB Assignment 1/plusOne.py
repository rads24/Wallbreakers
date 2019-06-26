class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        finalVal = int(s) + 1
        output = []
        for char in str(finalVal):
            output.append(int(char))
        return output