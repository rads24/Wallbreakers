class Solution:
    
    def divisibleByDigits(self, number: int):
        if ("0" in str(number)):
            return False
        temp = number
        while temp > 0:
            if ((number % (temp % 10)) == 0):
                temp = temp // 10
            else:
                return False
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfDividingNumbers = []
        for num in range(left, right + 1, 1):
            if (self.divisibleByDigits(num)):
                selfDividingNumbers.append(num)
        return selfDividingNumbers