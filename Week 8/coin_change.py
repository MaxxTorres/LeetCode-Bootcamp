from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with amount+1 (represents "infinity")
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Build up the solution
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
