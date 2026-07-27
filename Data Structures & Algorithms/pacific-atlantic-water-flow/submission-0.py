class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()
        # seen = set()
        def dfs(r, c, seen): # is recursive
            q = collections.deque()
            q.append((r, c))
            seen.add((r, c))
            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
                        seen.add((nr, nc))
        for i in range(len(heights[0])):
            dfs(0, i, pacific)
            dfs(len(heights) - 1, i, atlantic)
        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0]) - 1, atlantic)
        return list(pacific.intersection(atlantic))