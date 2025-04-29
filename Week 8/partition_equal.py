from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # If total is odd, cannot split into two equal subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        # dp[i] = True if a subset with sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero sum is always possible
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
