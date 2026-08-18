class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            # skip duplicate i
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = n - 1
            target = -1 * (nums[i])
            while l < r:
                x = nums[l] + nums[r]
                if x == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif x < target:
                    # l shifts forward; skip the current nums[l]
                    l += 1
                    # while l < r and nums[l] == nums[l-1]:
                    #     l += 1
                else:
                    r -= 1
                    # while l < r and nums[r] == nums[r+1]:
                    #     r -= 1
        return res