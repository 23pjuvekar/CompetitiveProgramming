class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        components = n
        parent = list(range(n))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal components
            px = find(x)
            py = find(y)
            
            if px != py:
                parent[py] = px
                components -=1

        for u, v in connections:
            union(u, v)
        
        return components - 1
