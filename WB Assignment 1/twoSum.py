class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # loop through the list, check if the target-current number exists in the remaining list, return the current index and index of number in the list
        
        for i, num in enumerate(nums):
            temp = target - num
            if temp in nums[i + 1:]:
                index = nums[i+1:].index(temp) + i + 1
                return [i, index]