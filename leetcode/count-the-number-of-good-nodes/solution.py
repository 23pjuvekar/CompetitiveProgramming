class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        memo = {}

        def get_size(curr: int, parent: int) -> int:
            if curr in memo:
                return memo[curr]
            
            size = 1
            for nbr in graph[curr]:
                if nbr != parent:
                    size += get_size(nbr, curr)
            
            memo[curr] = size
            return size

        get_size(0, -1)

        result = 0
        for i in range(n):
            children_sizes = set()
            for nbr in graph[i]:
                if memo[nbr] < memo[i]:
                    children_sizes.add(memo[nbr])
            
            if len(children_sizes) <= 1:
                result += 1
                
        return result
