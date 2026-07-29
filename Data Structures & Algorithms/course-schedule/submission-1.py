class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # there should be no cycles in graph -> DFS
        # cycles in arrs -> adj list
        adj = { i : [] for i in range(numCourses)}
        for x, y in prerequisites:
            adj[x].append(y)
        seen = set()
        # now; dfs
        def dfs(x):
            if adj[x] == []:
                return True
            if x in seen:
                return False
            seen.add(x)
            for i in adj[x]:
                # seen.add(i)
                if not dfs(i):
                    return False
            # after we are done, remove i from seen (why??)
            seen.remove(x)
            adj[x] = []
            return True
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True
