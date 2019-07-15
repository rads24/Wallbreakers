class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        count20 = 0
        
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                if count5 >= 1:
                    count5 -= 1
                    count10 += 1
                else:
                    return False
            elif bill == 20:
                if count5 >= 1 and count10 >= 1:
                    count5 -= 1
                    count10 -= 1
                    count20 += 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        return True