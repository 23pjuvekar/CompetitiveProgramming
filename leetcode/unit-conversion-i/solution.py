class Solution:
    def baseUnitConversions(self, conversions: list[list[int]]) -> list[int]:
        n = len(conversions) + 1
        graph = [[] for _ in range(n)]
        
        for u, v, z in conversions:
            graph[u].append((v, z))
            
        ans = [0] * n
        mod = 10**9 + 7
        
        queue = deque([0])
        ans[0] = 1
        
        while queue:
            x = queue.popleft()
            for y, z in graph[x]:
                ans[y] = (ans[x] * z) % mod
                queue.append(y)
                
        return ans
