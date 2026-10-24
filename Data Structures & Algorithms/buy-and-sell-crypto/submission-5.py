class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1 # buy, sell
        best = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit > 0:
                if profit > best:
                    best = profit
                # i += 1
            else: # we have a new low price in j
                i = j
            j += 1
        return best