class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        
        while min <= max:
            avg = (min + max) // 2
            if nums[avg] == target:
                return avg
            elif nums[avg] < target:
                min = avg + 1
            else:
                max = avg - 1
        return -1