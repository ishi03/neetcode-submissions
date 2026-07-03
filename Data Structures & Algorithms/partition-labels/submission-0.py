class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {}
        for i in range(len(s)):
            ends[s[i]] = i
        end = 0
        count = 0
        res = []
        for i in range(len(s)):
            count += 1
            if ends[s[i]] > end:
                end = ends[s[i]]
            if i == end:
                res.append(count)
                count = 0
        return res