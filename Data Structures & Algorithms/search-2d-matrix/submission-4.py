class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)-1

        while lo <= hi:
            mid = (lo + hi) // 2
            if  target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][-1]:
                lo = mid + 1
            else: # matrix[mid][0] <= target <= matrix[mid][-1]
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                return False
        return False