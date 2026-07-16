class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c, i):
            if i == len(word):
                return True # why
            if r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] != word[i] or (r, c) in seen:
                return False
            seen.add((r, c))
            res = False
            for row, col in directions:
                res = res or dfs(r + row, c + col, i + 1)
            seen.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False