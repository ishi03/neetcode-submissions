class Solution:
    def climbStairs(self, n: int) -> int:
        # only requires the last 2 states
        # memoization
        # memo = {1:1, 2:2}
        # def fn(n):
        #     if n in memo:
        #         return memo[n]
        #     return fn(n-1) + fn(n-2)
        # return fn(n)
        
        # tabulation
        # dp = [0] * (n)
        # dp[0] = 1 # 1 step
        # dp[1] = 2 # 2 step
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[-1]

        # constant space
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev, curr = 1, 2
        for i in range(2, n):
            curr, prev = curr + prev, curr
        return curr