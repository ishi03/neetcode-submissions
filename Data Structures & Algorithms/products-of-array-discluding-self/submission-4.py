class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        n = len(nums)
        res = [1] * n
        # go forward
        curr = 1
        for i in range(1, n):
            curr *= nums[i-1]
            res[i] = curr
        # go backwards
        curr = 1
        for i in range(n-2, -1, -1):
            curr *= nums[i+1]
            res[i] *= curr
        return res