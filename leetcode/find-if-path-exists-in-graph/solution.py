class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph_map = defaultdict(list)

        for x, y in edges:
            graph_map[x].append(y)
            graph_map[y].append(x)
        
        q = deque()
        q.append(source)
        visited = set()

        while q:
            vertex = q.popleft()
            visited.add(vertex)
            if vertex == destination:
                return True
            for new_edges in graph_map[vertex]:
                if new_edges not in visited:
                    q.append(new_edges)
        return False
