class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        seen = set()
        best = 0
        while i <= j and j < len(s):
            while s[j] in seen and i < j:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            best = max(best, len(seen))
            j += 1
        return best