class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        colors = defaultdict(int)
        last_color = {}
        res = []
        for i, c in queries:
            colors[c] += 1
            if i in last_color:
                colors[last_color[i]] -= 1
                if colors[last_color[i]] == 0:
                    del colors[last_color[i]]
            last_color[i] = c
            res.append(len(colors))
        return res
