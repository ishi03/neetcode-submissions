class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0 for _ in range(n1+1)] for _ in range(n2+1)]

        for i in range(n1+1):
            dp[0][i] = i
        for i in range(n2+1):
            dp[i][0] = i

        for j in range(1, n2+1):
            for i in range(1, n1+1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
        return dp[n2][n1]