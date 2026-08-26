class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        # odd palindromes
        for x in range(n):
            i, j = x, x
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                else:
                    count += 1
                    i -= 1
                    j += 1
         # even palindromes
        for x in range(n):
            i, j = x, x+1
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                else:
                    count += 1
                    i -= 1
                    j += 1
        return count  