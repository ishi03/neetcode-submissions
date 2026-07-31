class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list, cycle detection
        # Topological sort
        adj = {i: [] for i in range(numCourses)}
        seen = set()

        for x, y in prerequisites:
            adj[x].append(y)
        # each course can have 3 states
        # visited, visiting, unvisited
        output = []
        visited = set() # like seen/explored already
        visiting = set() # like current path
        def dfs(x):
            if x in visiting: # cycle
                return False
            if x in visited:
                return True
            visiting.add(x)
            for pre in adj[x]:
                if dfs(pre) == False: # cycle
                    return False
            visited.add(x)
            visiting.remove(x)
            output.append(x)
            return True
        for x in range(numCourses):
            if dfs(x) == False: # cycle
                return []
        return output