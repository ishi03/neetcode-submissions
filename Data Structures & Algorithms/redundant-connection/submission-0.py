class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initially it has n-1 edges
        # means it has n nodes
        n = len(edges) # n-1+1
        parent = [i for i in range(n + 1)] # 0 is unused; nodes start at 1
        rank = [1 for i in range(n + 1)]

        def find(n1): # find parent
            while n1 != parent[n1]:
                parent[n1] = parent[parent[n1]]
                n1 = parent[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # redundant connection
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p2] = parent[p1]
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            