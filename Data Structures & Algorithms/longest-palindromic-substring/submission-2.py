class Solution:
    def longestPalindrome(self, s: str) -> str:
        # THIS IS NOT DP
        # for odd length
        best = ""
        bestL = 0
        for x in range(len(s)):
            i, j = x, x
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                if len(s[i: j+1]) > bestL:
                    best = s[i: j+1]
                    bestL = len(s[i: j+1])
                i -= 1
                j += 1
        # for even length
        for x in range(len(s)):
            i, j = x, x+1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                if len(s[i: j+1]) > bestL:
                    best = s[i: j+1]
                    bestL = len(s[i: j+1])
                i -= 1
                j += 1
        return best
                