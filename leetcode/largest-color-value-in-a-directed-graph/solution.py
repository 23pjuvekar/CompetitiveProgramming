class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        n = len(colors)
        adj = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        dp = [[0] * 26 for _ in range(n)]

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                color_idx = ord(colors[i]) - ord('a')
                dp[i][color_idx] = 1

        nodes_visited = 0
        max_color_val = 0

        while q:
            u = q.popleft()
            nodes_visited += 1
            
            max_color_val = max(max_color_val, max(dp[u]))
            
            for v in adj[u]:
                u_color_idx = ord(colors[v]) - ord('a')
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == u_color_idx else 0))
                
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if nodes_visited < n:
            return -1
            
        return max_color_val
