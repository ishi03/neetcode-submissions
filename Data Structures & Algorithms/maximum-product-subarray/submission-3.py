class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # for each index, record the max product
        n = len(nums)
        res = nums[0]
        minProd = 1
        maxProd = 1
        for i in range(n):
            temp = minProd
            minProd = min(nums[i] * minProd, nums[i] * maxProd, nums[i])
            maxProd = max(nums[i] * temp, nums[i] * maxProd, nums[i])
            res = max(res, maxProd)

        return res