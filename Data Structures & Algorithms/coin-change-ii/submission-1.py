class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        # for i in range(len(coins)):
        #     dp[i][0] = 1

        for i in range(len(coins)-1, -1, -1):
            # bottom up; how many ways using coin and hence
            coin = coins[i]
            dp[i][0] = 1
            for amt in range(1, amount + 1):
                if amt >= coin:
                    dp[i][amt] = dp[i][amt-coin]
                if i < len(coins)-1:
                    dp[i][amt] += dp[i+1][amt]

        return dp[0][amount]