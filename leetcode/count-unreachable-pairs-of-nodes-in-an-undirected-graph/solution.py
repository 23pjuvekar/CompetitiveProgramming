class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node: int) -> int:
            count = 1
            visit[node] = True
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    count += dfs(neighbor)
            return count

        visit = [False] * n
        number_of_pairs = 0
        remaining_nodes = n

        for i in range(n):
            if not visit[i]:
                size_of_component = dfs(i)
                number_of_pairs += size_of_component * (remaining_nodes - size_of_component)
                remaining_nodes -= size_of_component

        return number_of_pairs
