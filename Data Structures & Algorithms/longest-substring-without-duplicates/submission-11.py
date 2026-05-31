class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        seen = set()
        best = 0
        # seen.add(s[0])
        while slow <= fast and fast < len(s):
            if s[fast] not in seen:
                seen.add(s[fast])
                best = max(best, fast - slow + 1)
            else: # fast is in seen
                while s[fast] in seen and slow < fast:
                    seen.remove(s[slow])
                    slow += 1
                seen.add(s[fast])
                best = max(best, fast - slow + 1)
            fast += 1
        return best