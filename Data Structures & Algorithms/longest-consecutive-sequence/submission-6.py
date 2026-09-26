class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for el in nums:
            if el - 1 in nums:
                continue
            else:
                l = 1
                while el + 1 in nums:
                    l += 1
                    el += 1
                best = max(best, l)
        return best