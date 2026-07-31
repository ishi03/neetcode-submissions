class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # this problem is cycle detection in DAG
        # one alt soln is checking tree properties: n-1 edges +
        # dfs traversal to check all n nodes are reachable/connected
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        seen = set()

        def dfs(x, prev):
            if x in seen: #
                return False
            seen.add(x)
            for y in adj[x]:
                if y == prev:
                    continue
                if not dfs(y, x): # this line is imp for bool dfs
                    return False
            return True # the whole removing from seen is hard to understnad
            # when to remove and when not too
            # depends on what seen reps; seen vs path
         
        return dfs(0, -1) and n == len(seen)
            