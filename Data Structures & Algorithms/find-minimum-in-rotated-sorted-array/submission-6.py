class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        curr = float('inf')
        while lo <= hi:
            if nums[lo] <= nums[hi]:
                # this is a sorted array
                curr = min(curr, nums[lo])
                break
            mid = (lo + hi) // 2
            curr = min(curr, nums[mid])
            if nums[lo] <= nums[mid]: # this bit is sorted, we alr checked
            # against lo
                lo = mid + 1 # explore the other side
            else:
                hi = mid - 1
        return curr

        # lo, hi = 0, len(nums) - 1
        # curr = float('inf')
        # while lo <= hi:
        #     # in binary search, the target IS in the range lo to hi
        #     # with that belief, the minimum is at lo
        #     if nums[lo] <= nums[hi]:
        #         curr = min(curr, nums[lo])
        #         break
        #     mid = (lo + hi) // 2
        #     curr = min(curr, nums[mid])
        #     if nums[lo] <= nums[mid]: # this half is sorted, we alr compared the lo
        #     # check in other half
        #         lo = mid + 1
        #     else: # the other half is the sorted one
        #         hi = mid - 1
        # return curr   
            