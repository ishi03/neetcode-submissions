class Solution:
    def rob(self, nums: List[int]) -> int:
        # const space
        def fn(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums)
            prev, curr = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                curr, prev = max(curr, prev + nums[i]), curr
            return curr
        if len(nums) == 1:
            return nums[0]
        return max(fn(nums[1:]), fn(nums[:-1]))