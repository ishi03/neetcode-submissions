class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 + n2 != len(s3):
            return False
        
        dp = [[False for _ in range(n1+1)] for _ in range(n2+1)]
        dp[0][0] = True

        for r in range(n2+1):
            for c in range(n1+1):
                if c > 0 and dp[r][c-1] and s1[c-1] == s3[r+c-1]:
                    dp[r][c] = True
                elif r > 0 and dp[r-1][c] and s2[r-1] == s3[r-1+c]:
                    dp[r][c] = True
        return dp[-1][-1]