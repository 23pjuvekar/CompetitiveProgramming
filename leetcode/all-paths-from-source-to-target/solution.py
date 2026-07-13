class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        

        q = deque()
        q.append([0])
        n = len(graph)
        res = []

        while q:
            node = q.popleft()
            if node[-1] == n - 1:
                res.append(node)
            else:
                for v in graph[node[-1]]:
                    new = node + [v]
                    q.append(new)
        return res
