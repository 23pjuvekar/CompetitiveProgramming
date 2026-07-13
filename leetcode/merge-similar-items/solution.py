class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        values = defaultdict(int)

        for key, amt in items1:
            values[key] += amt
        for key, amt in items2:
            values[key] += amt
        res = []
        for key, val in values.items():
            res.append([key, val])
        res.sort()
        return res
