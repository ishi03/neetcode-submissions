class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS; tier; snapshot
        l, r = 0, 0
        res  = 0
        while r < len(nums) - 1:
            # find the farthest we can go for this window
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            res += 1
        return res