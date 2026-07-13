class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph_map = {c : [] for c in range(n)}

        for e1, e2 in edges:
            graph_map[e1].append(e2)
            graph_map[e2].append(e1)

        visit = set()


        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for neighbors in graph_map[node]:
                if neighbors == prev:
                    continue
                if not dfs(neighbors, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
