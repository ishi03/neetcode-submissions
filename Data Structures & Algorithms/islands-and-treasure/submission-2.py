class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multisource BFS
        # BFS starts from each source at once
        # Each room gets filled by the closest treasure wave.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647

        seen = set()
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        dist = 0 # in case we overwrite treasure
        while q:
            for _ in range(len(q)): # snapshop of curr level; equal dist assigned
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in seen and grid[nr][nc] == INF:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            dist += 1