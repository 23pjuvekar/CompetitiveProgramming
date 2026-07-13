class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parents = [i for i in range(n)]
        rank = [1] * n

        def findParent(node):
            res = node

            while res != parents[res]:
                parents[res] = parents[parents[res]] # Optimization. Look at path reduction.
                res = parents[res]

            return res
    
        def union(node_1, node_2):
            p1 = findParent(node_1)
            p2 = findParent(node_2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]

            return 1


        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
