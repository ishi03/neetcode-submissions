class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, subset, summ):
            if summ == target:
                res.append(subset.copy())
                return
            elif summ > target or i >= len(candidates):
                return
            # include ith index
            # if i>0 and candidates[i] == candidates[i-1] and 
            subset.append(candidates[i])
            dfs(i+1, subset, summ + candidates[i])
            # exclude ith index
            # skip over all the duplicates
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subset, summ)
        dfs(0, [], 0)
        return res