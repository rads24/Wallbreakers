class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        strRep = []
        for i in range(1, n+1):
            if (i % 3 == 0 and i % 5 == 0):
                strRep.append(('FizzBuzz'))
            elif (i % 3 == 0):
                strRep.append(('Fizz'))
            elif (i % 5 == 0):
                strRep.append(('Buzz'))
            else:
                strRep.append(repr(i))
        return strRep
        