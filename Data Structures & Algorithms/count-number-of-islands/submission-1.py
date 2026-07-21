class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        seen = set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def bfs(i, j):
            q = collections.deque()
            # add to the q; add to seen
            q.append((i, j))
            seen.add((i, j))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        # add the new r, c in q to be explored
                        q.append((nr, nc))
                        seen.add((nr, nc)) # these go hand in hand
            return 1
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    count += bfs(i, j)
        return count
