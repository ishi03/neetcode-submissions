class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = max(nums)
        for x in nums:
            curSum += x
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum