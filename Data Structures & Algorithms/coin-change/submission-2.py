class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min ways to make 0 to amount
        coins.sort()
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            # i is the current amount we are trying to make
            minWays = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minWays = min(minWays, dp[diff] + 1)
            dp[i] = minWays
        return dp[amount] if dp[amount] < float('inf') else -1