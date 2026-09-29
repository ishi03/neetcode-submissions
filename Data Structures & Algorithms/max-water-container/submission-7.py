class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        n = len(heights)
        l, r = 0, n - 1
        while l < r:
            best = max(best, (r-l) * min(heights[r], heights[l]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best