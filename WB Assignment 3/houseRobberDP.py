class Solution:
    
    def normalRob(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[len(nums) - 1]
    
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        dp1 = self.normalRob(nums[0: len(nums)-1])
        dp2 = self.normalRob(nums[1: len(nums)])
        
        return max(dp1, dp2)