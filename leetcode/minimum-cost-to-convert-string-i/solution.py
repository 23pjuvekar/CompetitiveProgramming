class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        dist = [[math.inf] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for i in range(len(original)):
            u = ord(original[i]) - ord("a")
            v = ord(changed[i]) - ord("a")
            c = cost[i]
            dist[u][v] = min(dist[u][v], c)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res = 0
        for x, y in zip(source, target):
            if dist[ord(x) - ord("a")][ord(y) - ord("a")] == float("inf"):
                return -1
            res += dist[ord(x) - ord("a")][ord(y) - ord("a")]
        return res
