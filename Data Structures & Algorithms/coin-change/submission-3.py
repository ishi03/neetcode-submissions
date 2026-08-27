class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()
        for i in range(1, 1+amount):
            minWays = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minWays = min(minWays, dp[diff] + 1)
            dp[i] = minWays
        return dp[amount] if dp[amount] < float('inf') else -1
