class Solution:
    def climbStairs(self, n: int) -> int:
        # one way to get to 1
        # 2 ways to get to 2
        # for 3
        # once I get to 1 -> 1 way
        # once I get to 2 -> 2 way
        # for 4
        # once I get to 3 -> 1 way
        if n == 1:
            return 1
        one = 1
        two = 2
        # dp are for loops
        for i in range(n-2):
            temp = two
            two = one + two
            one = temp
        return two