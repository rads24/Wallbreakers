class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        profit = 0
        
        for value in prices:
            if value < minimum:
                minimum = value
            elif value - minimum > profit:
                profit = value - minimum
        return profit