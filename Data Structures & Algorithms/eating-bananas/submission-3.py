class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        best = hi
        while lo <= hi: # closed search space
            mid = (lo + hi) // 2
            # now consider eating speed is mid, does it satisfy?
            hrs = 0
            for x in piles:
                hrs += math.ceil(x/mid)
            if hrs > h: # no can't do
                lo = mid + 1
            else: # can we go lower?
                best = mid
                hi = mid - 1
        return best