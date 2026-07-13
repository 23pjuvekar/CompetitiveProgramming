class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        for [x, y], val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1/val
        def bfs(query):
            q = deque()
            visited = set()
            val = 1
            startVar, endVar = query
            q.append((startVar, val))
            while q:
                currentVar, currentVal = q.popleft()
                if currentVar == endVar and currentVar in graph:
                    return currentVal
                elif currentVar in graph:
                    visited.add(currentVar)
                    for nextVar in graph[currentVar].keys():
                        if nextVar not in visited:
                            q.append((nextVar, currentVal * graph[currentVar][nextVar]))
            return -1
        
        res = []
        for query in queries:
            res.append(bfs(query))
        return res
