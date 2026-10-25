class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            # if left is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]: # target is in there fs
                    hi = mid - 1
                else:
                    lo = mid + 1
            else: # right is sorted
                if nums[hi] >= target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
