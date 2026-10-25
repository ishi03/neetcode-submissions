class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)-1
        cols = len(matrix[0])-1
        ri, rj = 0, rows # lo, hi
        while ri <= rj:
            mid = (ri + rj) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols]:
                # this is our row
                i, j = 0, cols # lo, hi
                while i <= j:
                    m = (i + j) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif target < matrix[mid][m]:
                        # hi = mid - 1
                        j = m - 1
                    else:
                        i = m + 1
                return False
            elif target < matrix[mid][0]:
                # hi = mid - 1
                rj = mid - 1
            else:
                ri = mid + 1
        return False