class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        best = 0
        while j < len(prices) and i < j:
            if prices[i] < prices[j]:
                best = max(best, prices[j]-prices[i])
            else:
                i = j
            j += 1
        return best