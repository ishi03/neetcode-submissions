class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for x in nums:
            t = t ^ x
        return t