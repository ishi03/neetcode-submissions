class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = dict()
        cols = dict()
        boxs = dict()

        for i in range(9):
            for j in range(9):
                # ith row, jth col, i//3 j//3 box
                n = board[i][j]
                if n == ".":
                    continue
                if i not in rows:
                    rows[i] = set()
                if n in rows[i]:
                    return False
                else:
                    rows[i].add(n)
                
                if j not in cols:
                    cols[j] = set()
                if n in cols[j]:
                    return False
                else:
                    cols[j].add(n)

                if (i//3, j//3) not in boxs:
                    boxs[(i//3, j//3)] = set()
                if n in boxs[(i//3, j//3)]:
                    return False
                else:
                    boxs[(i//3, j//3)].add(n)
        return True