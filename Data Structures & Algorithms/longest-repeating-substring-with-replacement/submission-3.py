class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        maxL = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]]) # because this the the count altered
            # is our window valid?
            if (r - l + 1) - maxf > k: # invalid
                count[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL