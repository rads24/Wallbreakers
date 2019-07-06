class Solution:
    def square(self, n: int) -> int:
        strN = str(n)
        res = 0
        for char in strN:
            res += int(char) ** 2
        return res
            
    def isHappy(self, n: int) -> bool:
        # keep track of the numbers seen
        # if the new number generated is already seen before exit out of the loop and return false
        seen = set()
        seen.add(n)
        temp = n
        while True:
            happy = self.square(temp)
            if happy == 1:
                return True
            else:
                if happy in seen:
                    return False
                else:
                    seen.add(happy)
                    temp = happy
        