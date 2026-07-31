class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = max(nums) ## crux
        for x in nums:
            curSum += x
            if curSum < 0:
                curSum = 0
            else:
                maxSum = max(curSum, maxSum)
        return maxSum