class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        stones = set(S)
        jewelsInStones = stones.intersection(jewels)
        count = 0
        for stone in jewelsInStones:
            count += S.count(stone)
            
        return count