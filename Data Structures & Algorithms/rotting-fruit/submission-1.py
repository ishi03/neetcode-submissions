class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # For multi-source BFS with time:
        # - initial sources are time 0
        # - each BFS layer after that is +1 minute
        # - only keep going while there is still something fresh/unprocessed to convert
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = collections.deque()
        seen = set()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        t = 0
        while q and fresh > 0: # ensure we have something to go for
            for _ in range(len(q)):
                r, c = q.popleft()
                # if it is a fresh fruit; it is now rotten
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in seen and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        seen.add((nr, nc))
                        fresh -= 1
            t += 1

        if fresh > 0:
            return -1
        return t