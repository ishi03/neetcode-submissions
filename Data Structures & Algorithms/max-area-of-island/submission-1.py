class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        seen = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maxSz = 0

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))
            sz = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in seen and grid[nr][nc] == 1:
                        # we gotta explore this one
                        q.append((nr, nc))
                        seen.add((nr, nc))
                        sz += 1
            return sz

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    maxSz = max(maxSz, bfs(r, c))
        return maxSz