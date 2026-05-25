class Solution:
    def longestPalindrome(self, s: str) -> str:
        # THIS IS NOT DP, THIS IS 2 POINTER Q
        best = ""
        bestLen = 0
        # odd length
        for x in range(len(s)):
            i, j = x, x
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                if len(s[i:j+1]) > bestLen:
                    best = s[i:j+1]
                    bestLen = len(s[i:j+1])
                i-=1
                j+=1
        # even length
        for x in range(len(s)):
            i, j = x, x+1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                if len(s[i:j+1]) > bestLen:
                    best = s[i:j+1]
                    bestLen = len(s[i:j+1])
                i-=1
                j+=1
        return best