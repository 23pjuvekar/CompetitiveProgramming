class Solution:
    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        queue = deque([0])
        visited = {0}
        layers = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == n - 1:
                    return layers
                for neighbor in adj_list[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            layers += 1
        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = [[i + 1] if i < n - 1 else [] for i in range(n)]
        answer = []
        for u, v in queries:
            adj_list[u].append(v)
            answer.append(self.bfs(n, adj_list))
        return answer
