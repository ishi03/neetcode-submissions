class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        best = 0
        while j < len(prices) and i < j:
            if prices[j] > prices[i]: # it is a profit
                profit = prices[j] - prices[i]
                best = max(best, profit)
            else: # we find a new best lowest price
                i = j
            j += 1
        return best