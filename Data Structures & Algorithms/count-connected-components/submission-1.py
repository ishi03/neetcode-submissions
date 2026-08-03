class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find.
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n1):
            # find the parent of n1
            while parent[n1] != n1:
                parent[n1] = parent[parent[n1]] # path compression
                n1 = parent[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 # non unionization, connected elements
            if rank[p1] > rank[p2]:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
            else:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]
            return 1

        total = n
        for n1, n2 in edges:
            total -= union(n1, n2)
        return total