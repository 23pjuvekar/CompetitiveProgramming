from collections import defaultdict, deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_map = defaultdict(list)
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        visited = set()
        res = 0

        for i in range(n):
            if i not in visited:
                component_size = 0
                edge_count = 0
                q = deque()
                q.append(i)

                while q:
                    node = q.popleft()
                    if node not in visited:
                        visited.add(node)
                        component_size += 1
                        edge_count += len(edge_map[node])
                        for neighbor in edge_map[node]:
                            if neighbor not in visited:
                                q.append(neighbor)

                edge_count //= 2

                if edge_count == (component_size * (component_size - 1)) // 2:
                    res += 1

        return res
