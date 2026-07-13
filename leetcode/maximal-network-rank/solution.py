class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree_map = defaultdict(set)
        res = 0

        for road in roads:
            degree_map[road[0]].add(road[1])
            degree_map[road[1]].add(road[0])

        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                temp = len(degree_map[node1]) + len(degree_map[node2])
                if node2 in degree_map[node1]:
                    temp -= 1
                res = max(res, temp)
        
        return res
