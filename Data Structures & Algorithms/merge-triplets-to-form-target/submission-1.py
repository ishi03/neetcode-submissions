class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        strikes = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for n, x in enumerate(t):
                if x == target[n]:
                    strikes.add(n)
        return len(strikes) == 3