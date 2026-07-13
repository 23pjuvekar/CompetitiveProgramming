class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(list)
        degree_count = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree_count[u] += 1
            degree_count[v] += 1

        odd = []

        for node, degree in degree_count.items():
            if degree % 2 == 1:
                odd.append(node)

        if len(odd) == 0:
            return True

        if len(odd) == 2:
            if odd[0] not in graph[odd[1]]:
                return True
            for node in range(1, n + 1):
                if odd[0] not in graph[node] and odd[1] not in graph[node]:
                    return True
        
        if len(odd) == 4:
            if odd[0] not in graph[odd[1]] and odd[2] not in graph[odd[3]]:
                return True
            if odd[0] not in graph[odd[2]] and odd[1] not in graph[odd[3]]:
                return True
            if odd[0] not in graph[odd[3]] and odd[2] not in graph[odd[1]]:
                return True


        return False
