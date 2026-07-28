class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set() # set to remove at last

        def dfs(r, c):
            q = collections.deque()
            q.append((r, c))
            seen.add((r, c))
            while q:
                r, c = q.pop() # stack; dfs
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in seen and board[nr][nc] == "O":
                        q.append((nr, nc))
                        seen.add((nr, nc))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0]) - 1) and board[i][j] == "O":
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"