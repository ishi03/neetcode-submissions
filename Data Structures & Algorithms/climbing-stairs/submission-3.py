class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one = 1
        two = 2
        for i in range(n-2):
            temp = two
            two = one + two
            one = temp
        return two