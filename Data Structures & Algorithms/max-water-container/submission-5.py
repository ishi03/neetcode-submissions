class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAr = (r - l) * min(heights[l], heights[r])
        while l < r:
            ar = (r - l) * min(heights[l], heights[r])
            maxAr = max(maxAr, ar)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxAr