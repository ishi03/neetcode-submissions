class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            best = max(best, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best