class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        best = 0
        i, j = 0, 0
        maxf = 0
        # currl = 0
        # in freq we maintain the freq of letters in the current window
        while j < len(s) and i <= j:
            if s[j] not in freq:
                freq[s[j]] = 1
            else:
                freq[s[j]] += 1
            if freq[s[j]] > maxf:
                maxf = freq[s[j]]
            # if curr window len - maxf < k, we are good
            while (j - i + 1) - maxf > k:
                # shrink window till invalid (?)
                freq[s[i]] -= 1
                i += 1
            best = max(best, (j - i + 1))
            j += 1
        return best
