class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        mp = [[] for _ in range(n)]
        for x, y in edges:
            mp[x].append(y)
            mp[y].append(x)
        q = deque()
        q.append(0)
        seen = set()
        restricted = set(restricted)
        res = 0
        while q:
            node = q.popleft()
            if node not in restricted:
                res += 1
            seen.add(node)
            for node_new in mp[node]:
                if node_new not in seen and node_new not in restricted:
                    q.append(node_new)
        return res
