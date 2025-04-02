class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        
        total = 0
        
        for day in range(1, n + 1):
            if day >= delay:
                dp[day] = (dp[day] + dp[day - delay]) % MOD
            
            if day >= forget:
                dp[day] = (dp[day] - dp[day - forget]) % MOD
            
            total = (total + dp[day]) % MOD
        
        return total
