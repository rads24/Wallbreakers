class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        uniqueCandies = set(candies)
        
        return min(len(uniqueCandies), len(candies) // 2)