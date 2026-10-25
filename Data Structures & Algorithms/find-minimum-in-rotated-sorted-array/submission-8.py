class Solution:
    def findMin(self, nums: List[int]) -> int:
        best = float('inf')
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[lo] <= nums[mid]: # this is sorted
            # lowest here will be at lo;
                best = min(best, nums[lo])
                # now check for a lower value in next segment
                lo = mid + 1
            else:
                #the other half is sorted
                # lowest here is mid
                best = min(best, nums[mid])
                # now check for a lower value in next segment
                hi = mid - 1
        return best