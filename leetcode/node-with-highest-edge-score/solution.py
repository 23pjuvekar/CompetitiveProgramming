class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        edge_scores = defaultdict(int)
        for i in range(len(edges)):
            edge_scores[edges[i]] += i
        
        max_scores = 0
        res = 0
        for key, val in edge_scores.items():
            if val > max_scores:
                max_scores = val
                res = key
            elif val == max_scores:
                res = min(res, key)
        return res
