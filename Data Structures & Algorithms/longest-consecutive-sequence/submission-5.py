class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        eles = set(nums)
        maxx = 0
        for i in range(len(nums)):
            l = 1
            if nums[i]-1 in eles:
                continue
            x = nums[i]
            while x + 1 in eles:
                l += 1
                x += 1
            maxx = max(maxx, l)
        return maxx 