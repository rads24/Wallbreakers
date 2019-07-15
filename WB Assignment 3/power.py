class Solution:
    def power(self, x, n):
        if n == 1:
            return x
        elif n % 2 == 0:
            return self.power(x*x, n//2) 
        else:
            return x * self.power(x*x, n//2) 
        
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        elif n > 0:
            return self.power(x, n)
        else:
            n = abs(n)
            return 1/self.power(x,n)