class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        best = 0
        seen = set()
        while j < len(s) and i <= j:
            while s[j] in seen and i <= j:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            best = max(best, j - i + 1)
            j += 1
        return best