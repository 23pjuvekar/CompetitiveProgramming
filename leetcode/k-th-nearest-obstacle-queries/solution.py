class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        max_heap = []
        res = []
        for x, y in queries:
            heappush(max_heap, -(abs(x) + abs(y)))
            if len(max_heap) > k:
                heappop(max_heap)
            if len(max_heap) == k:
                res.append(-max_heap[0]) 
            else:
                res.append(-1)
        return res
