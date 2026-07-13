class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dp = defaultdict(list)
        n = len(colors)
        for i in range(n):
            dp[colors[i]].append(i)
        res = []
        for index, q in queries:
            if q not in dp:
                res.append(-1)
                continue
            indices = dp[q]
            i = bisect.bisect_left(indices, index)
            min_dist = float("inf")
            if 0 <= i - 1 < len(indices):
                min_dist = min(min_dist, abs(index - indices[i - 1]))
            if 0 <= i < len(indices):
                min_dist = min(min_dist, abs(index - indices[i]))
            res.append(min_dist if min_dist != float("inf") else -1)
        return res
