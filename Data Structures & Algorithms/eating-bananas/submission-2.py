class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        best = max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x/mid)
            if hours > h:
                # try for lesser number of hours -> more mid
                lo = mid + 1
            else:
                best = min(best, mid)
                # try for less hours -> more mid
                hi = mid - 1
        return best
