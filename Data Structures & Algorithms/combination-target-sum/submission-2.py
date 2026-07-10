class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # subset = []

        def dfs(i, subset, summ):
            # check if we are done w current branch
            if summ == target:
                res.append(subset.copy())
                return
            elif summ > target or i >= len(nums):
                return
            # include ith index
            subset.append(nums[i])
            dfs(i, subset, summ + nums[i])
            # exclude ith index
            subset.pop()
            dfs(i+1, subset, summ)
        dfs(0, [], 0)
        return res