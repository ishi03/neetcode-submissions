class Solution:
    def rob(self, nums: List[int]) -> int:
        def dynam(arr):
            n = len(arr)
            if n < 2:
                return arr[0]
            # n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[n-1]
        # we can not rob first and last house together
        if len(nums) < 2:
            return nums[0]
        return max(dynam(nums[1:]), dynam(nums[:-1]))