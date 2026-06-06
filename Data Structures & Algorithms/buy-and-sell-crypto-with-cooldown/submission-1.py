class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at each step, we can either buy or sell
        memo = {}
        def dp(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            if buying:
                # buy or cooldown day
                # buy
                buy = dp(i + 1, not buying) - prices[i] # we give this amt for neetcoin
                cooldown = dp(i + 1, buying)
                memo[(i, buying)] = max(buy, cooldown)
            else:
                # sell or cooldown
                sell = dp(i + 2, not buying) + prices[i]
                cooldown = dp(i + 1, buying)
                memo[(i, buying)] = max(sell, cooldown)
            return memo[(i, buying)]
        return dp(0, True)