class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for x in nums:
                if x not in subset:
                    subset.append(x)
                    dfs(subset)
                    subset.pop()
                    # dfs(subset)
                    # this has multiple branches; after undo we try next number
        dfs([])
        return res